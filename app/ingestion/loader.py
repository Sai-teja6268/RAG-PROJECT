from pathlib import Path
from typing import Any, List

from langchain_community.document_loaders import CSVLoader, PyMuPDFLoader


def load_all_documents(data_dir: str | Path) -> List[Any]:
    """Load supported documents from a directory."""
    data_path = Path(data_dir)
    documents: List[Any] = []
    print(f"[DEBUG] Loading documents from: {data_path}")

    pdf_files = list(data_path.glob("*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files.")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF file: {pdf_file}")
        try:
            loader = PyMuPDFLoader(str(pdf_file))
            docs = loader.load()
            documents.extend(docs)
            print(f"[DEBUG] Loaded {len(docs)} documents from {pdf_file}")
        except Exception as exc:
            print(f"[ERROR] Failed to load {pdf_file}: {exc}")

    csv_files = list(data_path.glob("*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files.")
    for csv_file in csv_files:
        print(f"[DEBUG] Loading CSV file: {csv_file}")
        try:
            loader = CSVLoader(str(csv_file))
            docs = loader.load()
            documents.extend(docs)
            print(f"[DEBUG] Loaded {len(docs)} documents from {csv_file}")
        except Exception as exc:
            print(f"[ERROR] Failed to load {csv_file}: {exc}")

    return documents

