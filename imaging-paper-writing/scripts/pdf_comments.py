#!/usr/bin/env python3
"""Extract a reviewer's annotations from a PDF: each highlight or note, the comment text, and the passage it marks.

Usage:
    python scripts/pdf_comments.py annotated.pdf
    python scripts/pdf_comments.py annotated.pdf --json

Why this exists: when a PDF is rendered to an image, highlights are visible but the text typed into a comment is not,
so the reason for a highlight is lost. This reads the annotation objects directly.

Requires PyMuPDF (`pip install pymupdf`). If the project runs in containers, install it into a throwaway container
rather than the project image. The script only reads the PDF.

A highlight with an empty comment carries no reason. Report it as "highlighted, no note" and ask the author what it
means; do not guess whether it marks something unclear or something to emphasize.
"""
from __future__ import annotations

import argparse
import json
import sys


def load_fitz():
    try:
        import pymupdf as fitz  # PyMuPDF >= 1.24
        return fitz
    except ImportError:
        try:
            import fitz
            return fitz
        except ImportError:
            print("PyMuPDF is not installed. Run: pip install pymupdf  (or use a throwaway container)", file=sys.stderr)
            raise SystemExit(2)


def marked_text(fitz, page, annot, words) -> str:
    """Words covered by a highlight/underline/strikeout; for notes, the words next to the icon."""
    if annot.vertices:
        v = annot.vertices
        rects = [fitz.Quad(v[i:i + 4]).rect for i in range(0, len(v) - 3, 4)]
        picked = []
        for w in words:
            wr = fitz.Rect(w[:4])
            area = wr.get_area() or 1.0
            if any((wr & r).get_area() > 0.5 * area for r in rects if wr.intersects(r)):
                picked.append(w[4])
        return " ".join(picked)
    r = annot.rect + (-2, -2, 80, 2)
    return "[near] " + " ".join(w[4] for w in words if fitz.Rect(w[:4]).intersects(r))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--json", action="store_true", help="print a JSON list instead of text")
    ap.add_argument("--width", type=int, default=400, help="maximum characters of marked text to print (default 400)")
    args = ap.parse_args()

    fitz = load_fitz()
    doc = fitz.open(args.pdf)
    rows = []
    for pno, page in enumerate(doc, 1):
        words = page.get_text("words")
        for annot in page.annots() or []:
            kind = annot.type[1]
            if kind in ("Link", "Widget", "Popup"):
                continue
            info = annot.info or {}
            rows.append({
                "page": pno,
                "type": kind,
                "author": info.get("title", ""),
                "comment": (info.get("content") or "").strip(),
                "text": " ".join(marked_text(fitz, page, annot, words).split()),
            })

    if args.json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return 0
    if not rows:
        print("No annotations found. If the reviewer's marks are visible in a viewer, the PDF may have been flattened "
              "(printed to PDF); ask for the original annotated file.")
        return 0
    silent = 0
    for i, r in enumerate(rows, 1):
        note = r["comment"] or "(highlighted, no note)"
        silent += not r["comment"]
        who = f" [{r['author']}]" if r["author"] else ""
        print(f"{i:>3}. p{r['page']} {r['type']}{who}: {note}")
        if r["text"]:
            print(f"     on: \"{r['text'][:args.width]}{'...' if len(r['text']) > args.width else ''}\"")
    print(f"\n{len(rows)} annotations; {silent} without a note (ask what these mean).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
