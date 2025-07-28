
# 📁 Adobe India Hackathon 2025 (Rounds 1A & 1B)

A suite of intelligent document processing solutions developed for Adobe's *Persona-Driven Document Intelligence Hackathon*. Our tools combine lightweight Docker containers with advanced text analysis to extract structure and meaning from PDFs.

## 🎯 Challenge Overview

| Round | Task | Our Solution |
|-------|------|--------------|
| **1A** | PDF Outline Extraction | Smart heading detection using text heuristics and pattern analysis |
| **1B** | Persona-Based Relevance | ONNX-powered semantic search with persona understanding |

## 💡 Key Features

- **Lightweight & Fast**:
  - Docker images under 1GB
  - Processing in under 60 seconds
  - CPU-only execution
  - Minimal dependencies

- **Smart Processing**:
  - Intelligent heading detection
  - Persona-based relevance ranking
  - Context-aware analysis
  - Multi-document correlation

## 📁 Project Structure

```
Adobe-Hackathon/
├── Round_1a/                    # PDF Outline Extractor
│   ├── app/
│   │   ├── main.py             # Processing pipeline
│   │   ├── pdf_parser.py       # Heading detection
│   │   └── requirements.txt    # Dependencies
│   ├── input/                  # Test PDFs
│   ├── output/                 # Generated JSONs
│   └── Dockerfile             # Alpine-based setup
│
├── Round_1b/                    # Persona-Based Intelligence
│   ├── app/
│   │   ├── main.py             # Orchestration
│   │   ├── pdf_parser.py       # Content extraction
│   │   ├── ranker.py           # ONNX ranking
│   │   └── requirements.txt    # Dependencies
│   ├── Collection 1/           # Travel guides
│   ├── Collection 2/           # Acrobat tutorials
│   ├── Collection 3/           # Recipe guides
│   └── Dockerfile             # Multi-stage build
└── README.md                   # This file
```

## 🚀 Quick Start

### Round 1A: PDF Outline Extractor

```bash
# Build the image
docker build -t pdf-outline-extractor ./Round_1a

# Run container
docker run --rm \
  -v "$(pwd)/Round_1a/input:/app/input:ro" \
  -v "$(pwd)/Round_1a/output:/app/output" \
  pdf-outline-extractor
```

### Round 1B: Persona-Based Relevance

```bash
# Build the image
docker build -t persona-doc-intel ./Round_1b

# Run container (example with Collection 1)
docker run --rm \
  -v "$(pwd)/Round_1b/Collection 1:/workspace/input:ro" \
  -v "$(pwd)/Round_1b/Collection 1:/workspace/output" \
  persona-doc-intel
```

## 🔧 Technical Stack

| Component | Purpose | Used In |
|-----------|---------|---------|
| Python 3.11 | Core runtime | Both rounds |
| PyPDF2 3.0.1 | PDF parsing | Round 1A |
| PyMuPDF | Content extraction | Round 1B |
| ONNX MiniLM | Semantic ranking | Round 1B |
| SpaCy | Text processing | Round 1B |
| Alpine Linux | Container base | Both rounds |

## 💫 Design Philosophy

1. **Simplicity First**: 
   - Minimal dependencies
   - Clean, modular code
   - Straightforward deployment

2. **Smart Processing**:
   - Intelligent heuristics
   - Context awareness
   - Pattern recognition

3. **Performance Focus**:
   - Fast execution
   - Memory efficient
   - Resource conscious

## Team - Mental ACROBATics

### Members
- Raghav Manchanda
- Arjun Chouksey
- Pranjal Bhardwaj