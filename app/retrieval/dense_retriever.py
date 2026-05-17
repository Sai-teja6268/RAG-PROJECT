from typing import Any
import numpy as np

from app.vectorstores.faiss_store import FaissVectorStore
import logging


logger = logging.getLogger(__name__)

class DenseRetriever:
    def __init__(self):
        self.vector_store = FaissVectorStore()
        try:
            self.vector_store.load()
            logger.info(
                f"Dense index loaded. Total embeddings: {self.vector_store.index.ntotal if self.vector_store.index else 0}"
            )
        except Exception:
            logger.warning("No existing FAISS index found. A new one will be built.")

    def build_index(self, chunks) -> None:
        logger.info(f"Building dense index for {len(chunks)} chunks.")
        embeddings = self.vector_store.embedding_model.encode([chunk.page_content for chunk in chunks])
        metadatas = [{"text": chunk.page_content, **getattr(chunk, "metadata", {})} for chunk in chunks]
        self.vector_store.add_embeddings(np.array(embeddings).astype("float32"), metadatas)
        self.vector_store.save()

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        raw_results = self.vector_store.query(query, top_k=top_k)
        results = []
        for res in raw_results:
            # Convert L2 distance to a similarity score (higher is better) for reciprocal rank fusion
            score = 1.0 / (1.0 + res["distance"])
            meta = res["metadata"] or {}
            results.append({
                "score": score,
                "page_content": meta.get("text", ""),
                "metadata": meta
            })
        return results
