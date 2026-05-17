import numpy as np
from app.embeddings.embedding import EmbeddingsPipeline

class EmbeddingService:
    def __init__(self, embedding_pipeline: EmbeddingsPipeline):
        self.embedding_pipeline = embedding_pipeline

    def generate_query_embedding(self, query: str) -> np.ndarray:
        """Generate embeddings for a query string."""
        return self.embedding_pipeline.embed_query(query)
