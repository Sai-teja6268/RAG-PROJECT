from typing import Any, List

import numpy as np
from sentence_transformers import SentenceTransformer

from app.core.constants import DEFAULT_CHUNK_OVERLAP, DEFAULT_CHUNK_SIZE, DEFAULT_EMBEDDING_MODEL
from app.ingestion.chunker import chunk_documents


class EmbeddingsPipeline:
    def __init__(
        self,
        embedding_model: str | SentenceTransformer = DEFAULT_EMBEDDING_MODEL,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    ):
        self.model = (
            embedding_model
            if isinstance(embedding_model, SentenceTransformer)
            else SentenceTransformer(embedding_model)
        )
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_documents(self, documents: List[Any]) -> List[Any]:
        return chunk_documents(documents, self.chunk_size, self.chunk_overlap)

    def embed_query(self, query: str) -> np.ndarray:
        """Generate embeddings for a query string."""
        embedding = self.model.encode([query])[0]
        return embedding

