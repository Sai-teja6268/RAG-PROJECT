from pathlib import Path

from app.ingestion.pipeline import IngestionPipeline
from app.vectorstores.faiss_store import FaissVectorStore


class IngestionService:
    def __init__(self, pipeline: IngestionPipeline | None = None, vector_store: FaissVectorStore | None = None):
        self.pipeline = pipeline or IngestionPipeline()
        self.vector_store = vector_store or FaissVectorStore()

    def ingest(self, data_dir: str | Path) -> dict:
        documents = self.pipeline.load(data_dir)
        self.vector_store.build_from_documents(documents)
        return {"documents": len(documents), "persist_dir": self.vector_store.persist_dir}

