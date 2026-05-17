from pathlib import Path
from typing import Any, List

from app.ingestion.deduplicator import deduplicate_documents
from app.ingestion.loader import load_all_documents


class IngestionPipeline:
    def load(self, data_dir: str | Path) -> List[Any]:
        documents = load_all_documents(data_dir)
        return deduplicate_documents(documents)

