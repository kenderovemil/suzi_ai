# Suzi AI 📝🤖

**Suzi AI** is an intelligent assistant developed as a personal project by Emil (Lyumel).
Its purpose is to assist with text and document processing, extract information, create summaries and statistical analyses, and prepare data for language model training.

---

## ✨ Main features

- **Document processing**: PDF, DOCX, TXT, SQL, CSV
- OCR for scanned books and articles
- Text extraction and structuring in JSON
- Chunking for preparing datasets for fine-tuning
 

- **Summaries and retellings**
- Turns complex scientific or esoteric texts into clear, human explanations
- Supports adding personal notes and edits
 

- **Statistical analyses**
- Processing tables and financial documents
- Generating graphs and trends
- Preparing reports for business or scientific purposes
 

- **Vector search**
- FAISS/ChromaDB for quick retrieval of relevant passages
- Preparation of scientific research databases
 

- **Integrations**
- Ability to connect to external models (ChatGPT, Gemini)
- Prompt generator for graphics and animation

---

## 🛠️ Technologies

- **Python 3.10+**
- Hugging Face Transformers (LLM integration)
- LangChain (chunking, vector search)
- PyMuPDF, pdfplumber, python-docx (document processing)
- Tesseract/PaddleOCR (OCR)
- Pandas, NumPy, Matplotlib, Seaborn, Plotly (statistics and visualization)
- FastAPI (interface and REST API)
- FAISS/ChromaDB (vector databases)

---

## 📂 Project structure

SUZI AI/ ├── data/ # input data ├── interface/ # future UI ├── models/ # trained models ├── suzi_core/ # core logic │ ├── document_parser.py │ ├── ocr.py │ ├── summarizer.py │ ├── statistics.py │ └── vector_store.py ├── utils/ # utility functions │ ├── config.py │ ├── file_utils.py │ └── logger.py ├── requirements.txt # libraries ├── LICENSE # license (MIT) └── README.md # project description

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- Git with proper authentication configured (see [Contributing Guide](CONTRIBUTING.md#-github-authentication-setup))

### Quick Start

1. **Clone the repository:**
   ```bash
   # With SSH (recommended)
   git clone git@github.com:kenderovemil/suzi_ai.git
   
   # Or with HTTPS (requires Personal Access Token)
   git clone https://github.com/kenderovemil/suzi_ai.git
   ```

2. **Navigate to project directory:**
   ```bash
   cd suzi_ai
   ```

3. **Create and activate virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🤝 Contributing

We welcome contributions! Please check out our [Contributing Guide](CONTRIBUTING.md) for:
- GitHub authentication setup (SSH keys or Personal Access Tokens)
- Development workflow
- Code style guidelines
- How to submit pull requests

### Common Issues

**Getting a 403 error when pushing to GitHub?** 

GitHub no longer accepts passwords for Git operations. You need to use either SSH keys or a Personal Access Token. See the [Troubleshooting Guide](CONTRIBUTING.md#-troubleshooting-common-issues) for detailed solutions.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Emil (Lyumel)** - Personal AI Assistant Project
