#!/usr/bin/env python3
"""Inventory the experiments in a code project so the paper can be written from what was actually run.

Usage:
    python experiment_inventory.py PROJECT_DIR [--json] [--max-files 2000]

Prints a markdown report: git state, configs, result files, logs (with crash / NaN /
test-evaluation flags), checkpoints, notebooks, code-level leads, and an experiment
ledger skeleton with [confirm] placeholders.

Everything here is a heuristic lead. Read the code or log before drawing a conclusion.
The script only reads files. It never runs project code.
"""
import argparse
import json
import re
import subprocess
import time
from pathlib import Path

SKIP = {".git", "__pycache__", "node_modules", ".venv", "venv", "env", ".ipynb_checkpoints",
        ".mypy_cache", ".pytest_cache", ".idea", ".vscode", "site-packages"}
EXP_DIRS = {"wandb", "runs", "lightning_logs", "mlruns", "outputs", "results", "logs", "experiments", "checkpoints"}
CKPT_EXT = {".pt", ".pth", ".ckpt", ".h5", ".hdf5", ".safetensors", ".onnx", ".pkl", ".joblib"}
CFG_WORDS = re.compile(r"config|cfg|hparam|params|args|settings", re.I)
RES_WORDS = re.compile(r"result|metric|eval|summary|score|prediction|performance|ablation|benchmark", re.I)
MAX_READ = 5_000_000


def walk(root, limit):
    out = []
    for p in root.rglob("*"):
        if any(part in SKIP for part in p.parts):
            continue
        if p.is_file():
            out.append(p)
            if len(out) >= limit:
                break
    return out


def read(p):
    try:
        if p.stat().st_size > MAX_READ:
            with open(p, "rb") as f:
                f.seek(-MAX_READ, 2)
                return f.read().decode("utf-8", "replace")
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def git_info(root):
    def g(*a):
        try:
            return subprocess.run(["git", "-C", str(root), *a], capture_output=True, text=True, timeout=20).stdout.strip()
        except Exception:
            return ""
    if not (root / ".git").exists():
        return {"is_repo": False}
    return {"is_repo": True, "commit": g("rev-parse", "HEAD")[:12], "branch": g("rev-parse", "--abbrev-ref", "HEAD"),
            "dirty_files": len([x for x in g("status", "--porcelain").splitlines() if x]),
            "recent": g("log", "-n", "8", "--date=short", "--format=%h %ad %s").splitlines()}


def scan_log(p):
    txt = read(p)
    lines = txt.splitlines()
    tail = "\n".join(lines[-60:])
    flags = []
    if re.search(r"Traceback \(most recent call last\)", tail):
        flags.append("traceback near end (likely crashed)")
    if re.search(r"out of memory|\bKilled\b|KeyboardInterrupt|SIGTERM", tail, re.I):
        flags.append("OOM / killed / interrupted near end")
    if re.search(r"\b(loss|train_loss)\W{0,3}(nan|inf)\b", txt, re.I):
        flags.append("NaN/inf loss appears")
    if re.search(r"early stop", txt, re.I):
        flags.append("early stopping triggered")
    tests = [l for l in lines if re.search(r"\btest\b.*(dice|acc|auc|loss|f1|iou|psnr|ssim|metric)", l, re.I)]
    if len(tests) > 3:
        flags.append(f"test metrics printed {len(tests)} times (was the test set used during development?)")
    epochs = re.findall(r"[Ee]poch\W{0,3}(\d+)", txt)
    return {"lines": len(lines), "last_epoch": max(map(int, epochs)) if epochs else None, "flags": flags,
            "last_line": (lines[-1][:120] if lines else "")}


def scan_code(p):
    txt = read(p)
    leads = []
    if re.search(r"train_test_split|random_split|KFold\(|ShuffleSplit", txt) and not re.search(r"Group(Shuffle|K)?(Split|Fold)|StratifiedGroupKFold|groups\s*=", txt):
        leads.append("split call with no group-aware splitter or groups= argument: check the split is by patient, not slice or file")
    if re.search(r"\.fit(_transform)?\(", txt) and re.search(r"\btest\b", txt):
        leads.append("scaler/PCA/model .fit near test data: check it is fit on training data only")
    for i, l in enumerate(txt.splitlines(), 1):
        if re.search(r"\btest", l, re.I) and re.search(r"best|early_stop|save_?(ckpt|checkpoint|model)|argmax|threshold", l, re.I):
            leads.append(f"L{i}: test data near model/threshold selection: `{l.strip()[:90]}`")
    if re.search(r"for\s+epoch", txt) and re.search(r"test_loader|test_dataset|test_set|x_test", txt):
        leads.append("test data referenced in a file with a training loop: check it is not evaluated every epoch for selection")
    todo = len(re.findall(r"TODO|FIXME|HACK|XXX", txt))
    if todo:
        leads.append(f"{todo} TODO/FIXME/HACK markers")
    has_seed = bool(re.search(r"manual_seed|np\.random\.seed|random\.seed|seed_everything|default_rng|\bseed\b", txt))
    return leads, has_seed, bool(re.search(r"torch|tensorflow|jax|sklearn", txt))


def notebook_info(p):
    try:
        nb = json.loads(read(p))
        cells = [c for c in nb.get("cells", []) if c.get("cell_type") == "code"]
        return {"code_cells": len(cells), "with_outputs": sum(1 for c in cells if c.get("outputs")),
                "never_run": sum(1 for c in cells if c.get("execution_count") is None)}
    except Exception:
        return {"error": "could not parse"}


def mtime(p):
    return time.strftime("%Y-%m-%d", time.localtime(p.stat().st_mtime))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("project")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max-files", type=int, default=2000)
    a = ap.parse_args()
    root = Path(a.project).resolve()
    files = walk(root, a.max_files)

    cfgs, results, logs, ckpts, nbs, pys = [], [], [], [], [], []
    for p in files:
        rel = str(p.relative_to(root))
        ext = p.suffix.lower()
        if ext in CKPT_EXT:
            ckpts.append(p)
        elif ext == ".ipynb":
            nbs.append(p)
        elif ext == ".py":
            pys.append(p)
        elif ext in {".log", ".out", ".err"} or "tfevents" in p.name or (ext == ".txt" and re.search(r"train|log|eval", p.name, re.I)):
            logs.append(p)
        elif ext in {".yaml", ".yml", ".toml", ".json", ".cfg", ".ini"} and CFG_WORDS.search(p.name):
            cfgs.append(p)
        elif ext in {".csv", ".json", ".jsonl", ".tsv", ".xlsx"} and RES_WORDS.search(rel):
            results.append(p)

    report = {"project": str(root), "git": git_info(root), "files_scanned": len(files),
              "experiment_dirs": sorted(d.name for d in root.rglob("*") if d.is_dir() and d.name in EXP_DIRS and not any(x in SKIP for x in d.parts))[:20],
              "configs": [str(p.relative_to(root)) for p in cfgs],
              "results": [(str(p.relative_to(root)), mtime(p)) for p in results],
              "logs": {str(p.relative_to(root)): scan_log(p) for p in logs if "tfevents" not in p.name},
              "tfevents": [str(p.relative_to(root)) for p in logs if "tfevents" in p.name],
              "checkpoints": [(str(p.relative_to(root)), p.stat().st_size // 1_000_000, mtime(p)) for p in ckpts],
              "notebooks": {str(p.relative_to(root)): notebook_info(p) for p in nbs}}
    leads, seed_files, ml_files = {}, 0, 0
    for p in pys:
        l, s, ml = scan_code(p)
        if l:
            leads[str(p.relative_to(root))] = l
        ml_files += ml
        seed_files += (s and ml)
    report["code_leads"] = leads
    report["seed_note"] = ("no seed setting found in any ML code file" if ml_files and not seed_files
                           else f"seed setting found in {seed_files} of {ml_files} ML code files")

    if a.json:
        print(json.dumps(report, indent=2, default=str))
        return

    g = report["git"]
    print(f"# Experiment inventory: {root.name}\n")
    print("## Git")
    if g["is_repo"]:
        print(f"- commit {g['commit']} on {g['branch']}; {g['dirty_files']} uncommitted file(s)"
              + (" **(results may not match committed code)**" if g["dirty_files"] else ""))
        for r in g["recent"]:
            print(f"  - {r}")
    else:
        print("- not a git repository: no commit to cite; ask the user how to pin the code version")
    print(f"\n## Layout\n- {report['files_scanned']} files scanned. Experiment-style dirs: {', '.join(report['experiment_dirs']) or 'none'}")
    print("\n## Configs")
    for c in report["configs"]:
        print(f"- {c}")
    if not report["configs"]:
        print("- none found by name; configs may be CLI args or in code")
    print("\n## Result files (check mtimes against code changes)")
    for r, m in report["results"]: print(f"- {r} ({m})")
    if not report["results"]: print("- none found by name")
    print("\n## Logs")
    for name, info in report["logs"].items():
        print(f"- {name}: {info['lines']} lines, last epoch {info['last_epoch']}")
        for f in info["flags"]: print(f"  - FLAG: {f}")
    for t in report["tfevents"]: print(f"- {t} (tensorboard events; not parsed)")
    print("\n## Checkpoints")
    for c, mb, m in report["checkpoints"]: print(f"- {c} ({mb} MB, {m})")
    if not report["checkpoints"]: print("- none in this folder (may live elsewhere)")
    print("\n## Notebooks")
    for n, i in report["notebooks"].items():
        print(f"- {n}: {i}")
    print(f"\n## Code leads (read the code before concluding)\n- Seeds: {report['seed_note']}")
    for f, ls in leads.items():
        for l in ls: print(f"- {f}: {l}")
    print("\n## Experiment ledger skeleton (fill from files; ask the user for anything marked [confirm])\n")
    print("| Run ID | Purpose | Commit | Config | Data/split | Seeds | Status | Selection rule | Result file | In paper? |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    rows = list(report["logs"]) or [r for r, _ in report["results"]] or ["[run]"]
    for r in rows:
        print(f"| {Path(r).stem} | [confirm] | {g.get('commit', '[confirm]')} | [confirm] | [confirm] | [confirm] | [confirm] | [confirm] | {r} | [confirm] |")
    print("\nNot answerable from files: population, reference standard, ethics, which analyses were pre-specified, unrecorded runs.")


if __name__ == "__main__":
    main()
