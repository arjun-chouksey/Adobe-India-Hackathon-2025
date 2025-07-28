# 📄 Round 1A - Connecting the Dots Through Docs

An intelligent, lightweight solution that automatically extracts structured outlines from PDF documents. Built with Python and Docker, this tool uses advanced text heuristics to identify document structure without relying on PDF metadata or complex ML models.

## 🎯 Key Features

- **Smart Heading Detection**:
  - Pattern recognition for numbered sections (1.1, A., etc.)
  - Intelligent text analysis (casing, length, position)
  - Contextual hierarchy detection
  - Split heading merging
  
- **High Performance**:
  - Processes multiple PDFs in seconds
  - Memory efficient: <100MB RAM usage
  - Docker container size < 1GB
  - Pure Python implementation

- **Clean Output**:
  - Structured JSON format
  - Accurate page numbers
  - Hierarchical heading levels (H1-H3)
  - Merged split headings

## 🔧 Technical Implementation

```python
# Key heuristics used:
def extract_headings(pdf):
    # 1. Pattern matching for numbered sections
    # 2. Text position and formatting analysis
    # 3. Contextual hierarchy validation
    # 4. Split heading detection and merging
    return structured_outline
```

## 📁 Project Structure

```
.
├── app/
│   ├── main.py             # PDF processing pipeline
│   ├── pdf_parser.py       # Core extraction logic
│   └── requirements.txt    # Dependencies (PyPDF2)
├── input/                  # PDF input directory
├── output/                 # JSON output directory
└── Dockerfile             # Alpine-based container
```

## 📊 Sample Output

```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "1. Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "1.1 Background",
      "page": 2
    }
  ]
}
```

## 🚀 Quick Start

### Using Docker (Recommended)

1. Build the image:
```bash
docker build -t pdf-outline-extractor .
```

2. Run the container:
```bash
docker run --rm \
  -v "$(pwd)/input:/app/input:ro" \
  -v "$(pwd)/output:/app/output" \
  --platform linux/amd64 \
  pdf-outline-extractor
```

### Local Development

```bash
# Install dependencies
pip install -r app/requirements.txt

# Run the extractor
python app/main.py
```

## 🔍 How It Works

1. **Text Extraction**: Uses PyPDF2 to extract raw text while preserving layout
2. **Pattern Analysis**: Identifies heading patterns using regex and heuristics
3. **Hierarchy Detection**: Determines heading levels based on multiple factors
4. **Post-Processing**: Merges split headings and validates structure
5. **JSON Generation**: Creates clean, structured output

## 💡 Design Decisions

- **Why PyPDF2?** Lightweight, pure Python, no system dependencies
- **Why Docker?** Consistent environment, easy deployment
- **Why Heuristics?** Fast, reliable, no ML complexity


## Team - Mental ACROBATics

## Members
- Raghav Manchanda
- Arjun Chouksey
- Pranjal Bhardwaj