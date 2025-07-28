#!/usr/bin/env python3
import json, os
from pathlib import Path
from pdf_parser import extract_outline

INPUT_DIR  = Path("/app/input")
OUTPUT_DIR = Path("/app/output")

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for pdf in INPUT_DIR.glob("*.pdf"):
        out = OUTPUT_DIR / f"{pdf.stem}.json"
        out.write_text(json.dumps(extract_outline(str(pdf)), indent=2))
        print(f"{pdf.name}  →  {out.name}")

if __name__ == "__main__":
    main()