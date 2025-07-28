
from PyPDF2 import PdfReader
from typing import Dict, List, Optional
import re

def is_numbered_heading(text: str) -> bool:
    """Check if text starts with common heading number patterns."""
    patterns = [
        r'^\d+\.',  # "1."
        r'^\d+\.\d+',  # "1.1"
        r'^\d+\.\d+\.\d+',  # "1.1.1"
        r'^[A-Z]\.',  # "A."
        r'^\([a-z]\)',  # "(a)"
        r'^[IVXLC]+\.',  # Roman numerals
    ]
    return any(re.match(pattern, text.strip()) for pattern in patterns)

def merge_split_headings(lines: List[Dict]) -> List[Dict]:
    
    merged = []
    i = 0
    while i < len(lines):
        current = lines[i]
        # Look ahead for continuation
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            # If next line is very short and on same page, might be continuation
            if (next_line["page"] == current["page"] and 
                next_line["len"] < 20 and 
                not is_numbered_heading(next_line["text"])):
                current["text"] += " " + next_line["text"]
                current["len"] = len(current["text"])
                i += 2
                merged.append(current)
                continue
        merged.append(current)
        i += 1
    return merged

def validate_heading_level(text: str, prev_level: Optional[str] = None) -> bool:
    """Validate if this heading level makes sense in context."""
    if not text.strip():
        return False
    
    # Reject very short lines unless they're numbered
    if len(text) < 3 and not is_numbered_heading(text):
        return False
        
    # Reject common form field patterns
    form_patterns = [
        r'^Date',
        r'^Signature',
        r'^\s*$',  # Empty or whitespace
        r'^Name\s+Age',  # Table headers
        r'^Rs\.',  # Currency
    ]
    if any(re.match(pattern, text, re.I) for pattern in form_patterns):
        return False
    
    return True

def extract_outline(pdf_path: str) -> Dict:
    reader = PdfReader(pdf_path)
    lines = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if not text:
            continue
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            lines.append({
                "text": line,
                "len": len(line),
                "upper": line == line.upper(),
                "page": page_num
            })

    if not lines:
        return {"title": "No text", "outline": []}

    # Merge split headings first
    lines = merge_split_headings(lines)

    # thresholds
    max_len = max(l["len"] for l in lines)
    h1_len = max_len * 0.3  # Adjusted thresholds
    h2_len = max_len * 0.6
    h3_len = max_len * 0.8

    outline = []
    seen = set()
    prev_level = None
    
    for l in lines:
        if not validate_heading_level(l["text"], prev_level):
            continue
            
        lvl = None
        # Check for strong heading indicators
        if is_numbered_heading(l["text"]):
            if l["upper"]:
                lvl = "H1"
            elif "." in l["text"][:3]:  # Short number prefix
                lvl = "H2"
            else:
                lvl = "H3"
        # Fall back to length-based rules
        elif l["upper"] and l["len"] <= h1_len:
            lvl = "H1"
        elif l["upper"] and l["len"] <= h2_len:
            lvl = "H2"
        elif l["len"] <= h3_len and not l["text"].endswith('.'):  # Avoid sentences
            lvl = "H3"
            
        if lvl and l["text"] not in seen and validate_heading_level(l["text"], prev_level):
            outline.append({"level": lvl, "text": l["text"], "page": l["page"]})
            seen.add(l["text"])
            prev_level = lvl

    # Find title - prefer longer text on first page
    title_candidates = [l for l in lines if l["page"] == 1 and l["len"] > 20]
    title = (title_candidates[0]["text"] if title_candidates 
            else next((l["text"] for l in lines if l["page"] == 1), "Untitled"))

    # sort by page, then level
    outline = sorted(outline, key=lambda x: (x["page"], {"H1": 1, "H2": 2, "H3": 3}[x["level"]]))
    return {"title": title, "outline": outline}