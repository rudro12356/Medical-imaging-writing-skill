#!/usr/bin/env python3
"""Extract a co-author's review from a Word manuscript: comments, the text each comment is attached to, and tracked changes.

Usage:
    python scripts/docx_comments.py manuscript.docx              # comments, then tracked changes
    python scripts/docx_comments.py manuscript.docx --full-text  # also print the document with inline markers

Inline markers in --full-text:  [[C3: commented text]]   {+inserted text+}   [-deleted text-]

Standard library only. Reads the .docx directly; it does not modify the file.
A comment's anchor is the text between its range start and end; reviewers often select one word to stand for a whole
sentence, so the surrounding paragraph is printed as context.
"""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
import zipfile

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def read_xml(z: zipfile.ZipFile, name: str):
    try:
        return ET.fromstring(z.read(name))
    except KeyError:
        return None


def comment_table(z: zipfile.ZipFile) -> dict[str, dict]:
    root = read_xml(z, "word/comments.xml")
    out: dict[str, dict] = {}
    if root is None:
        return out
    for c in root.iter(W + "comment"):
        text = "\n".join("".join(t.text or "" for t in p.iter(W + "t")) for p in c.iter(W + "p")).strip()
        out[c.get(W + "id")] = {"author": c.get(W + "author", ""), "date": c.get(W + "date", ""), "text": text,
                                 "anchor": "", "paragraph": ""}
    return out


class Walker:
    """Walks one paragraph in document order, tracking open comment ranges and tracked-change state."""

    def __init__(self, comments: dict[str, dict]):
        self.comments = comments
        self.open: set[str] = set()
        self.changes: list[tuple[str, str, str]] = []  # (kind, author, text)

    def paragraph(self, p) -> tuple[str, str]:
        marked, plain = [], []
        touched: set[str] = set(self.open)

        def emit(text: str, ins: bool, dele: bool):
            if not text:
                return
            if dele:
                marked.append("[-" + text + "-]")
                return
            plain.append(text)
            marked.append("{+" + text + "+}" if ins else text)
            for cid in self.open:
                if cid in self.comments:
                    self.comments[cid]["anchor"] += text

        def walk(el, ins: bool, dele: bool, author: str):
            tag = el.tag
            if tag == W + "ins":
                ins, author = True, el.get(W + "author", "")
            elif tag == W + "del":
                dele, author = True, el.get(W + "author", "")
            if tag == W + "commentRangeStart":
                cid = el.get(W + "id")
                self.open.add(cid)
                touched.add(cid)
                marked.append(f"[[C{cid}: ")
            elif tag == W + "commentRangeEnd":
                self.open.discard(el.get(W + "id"))
                marked.append("]]")
            elif tag == W + "t":
                emit(el.text or "", ins, dele)
                if ins and el.text:
                    self.changes.append(("inserted", author, el.text))
            elif tag == W + "delText":
                emit(el.text or "", ins, True)
                if el.text:
                    self.changes.append(("deleted", author, el.text))
            elif tag == W + "tab":
                emit("\t", ins, dele)
            elif tag == W + "drawing":
                marked.append("[IMAGE]")
            elif tag.endswith("}oMath"):
                marked.append("[MATH]")
                return
            for child in el:
                walk(child, ins, dele, author)

        walk(p, False, False, "")
        text = "".join(plain)
        for cid in touched:
            if cid in self.comments and not self.comments[cid]["paragraph"]:
                self.comments[cid]["paragraph"] = text
        return "".join(marked), text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--full-text", action="store_true", help="print the whole document with inline markers")
    ap.add_argument("--context", type=int, default=220, help="characters of paragraph context per comment (default 220)")
    args = ap.parse_args()

    with zipfile.ZipFile(args.docx) as z:
        comments = comment_table(z)
        doc = read_xml(z, "word/document.xml")
    if doc is None:
        print("No word/document.xml found; is this a .docx file?", file=sys.stderr)
        return 2
    body = doc.find(W + "body")
    walker = Walker(comments)
    lines: list[str] = []

    def walk_block(node):
        for ch in node:
            if ch.tag == W + "p":
                style = ch.find(W + "pPr/" + W + "pStyle")
                marked, _ = walker.paragraph(ch)
                if marked.strip():
                    lines.append(f"[{style.get(W + 'val') if style is not None else ''}] {marked}")
            elif ch.tag == W + "tbl":
                lines.append("<TABLE>")
                for row in ch.iter(W + "tr"):
                    cells = [" ".join(walker.paragraph(p)[0] for p in cell.iter(W + "p")) for cell in row.iter(W + "tc")]
                    lines.append(" | ".join(cells))
                lines.append("</TABLE>")
            else:
                walk_block(ch)

    walk_block(body)

    if args.full_text:
        print("\n".join(lines))
        print()

    print(f"===== COMMENTS ({len(comments)}) =====")
    for cid, c in comments.items():
        anchor = " ".join(c["anchor"].split())
        para = " ".join(c["paragraph"].split())
        print(f"C{cid} [{c['author']}] {c['text']}")
        print(f"    on: \"{anchor[:args.context]}\"")
        if para and para != anchor:
            print(f"    in: \"{para[:args.context]}{'...' if len(para) > args.context else ''}\"")

    merged: list[list[str]] = []
    for kind, author, text in walker.changes:
        if merged and merged[-1][0] == kind and merged[-1][1] == author:
            merged[-1][2] += text
        else:
            merged.append([kind, author, text])
    print(f"\n===== TRACKED CHANGES ({len(merged)}) =====")
    for kind, author, text in merged:
        print(f"{kind} [{author}]: {' '.join(text.split())[:args.context]}")
    if not comments and not merged:
        print("(none found; the reviewer may have edited without tracking, so diff against the version you sent)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
