import os
import pickle
from typing import Any, List

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from app.core.constants import DEFAULT_CHUNK_OVERLAP, DEFAULT_CHUNK_SIZE, DEFAULT_EMBEDDING_MODEL
from app.embeddings.embedding import EmbeddingsPipeline


class FaissVectorStore:
    def __init__(
        self,
        persist_dir: str = "vector_store/faiss",
        embedding_model: str = DEFAULT_EMBEDDING_MODEL,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    ):
        self.embedding_model = SentenceTransformer(embedding_model)
        self.index = None
        self.persist_dir = persist_dir
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.metadata: list[Any] = []
        os.makedirs(self.persist_dir, exist_ok=True)

    def build_from_documents(self, documents: List[Any]) -> None:
        """Build FAISS index from documents."""
        print(f"[INFO] Building FAISS index from {len(documents)} documents.")
        emb_pipe = EmbeddingsPipeline(
            embedding_model=self.embedding_model,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )
        chunks = emb_pipe.chunk_documents(documents)
        embeddings = emb_pipe.chunk_embeddings(chunks)
        metadatas = [{"text": chunk.page_content, **getattr(chunk, "metadata", {})} for chunk in chunks]
        self.add_embeddings(np.array(embeddings).astype("float32"), metadatas)
        self.save()
        print(f"[INFO] FAISS index built and saved to {self.persist_dir}.")

    def add_embeddings(self, embeddings: np.ndarray, metadatas: List[Any]) -> None:
        print(f"[INFO] Adding {embeddings.shape[0]} embeddings to FAISS index.")
        dim = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        if metadatas:
            self.metadata.extend(metadatas)
        print(f"[INFO] Total embeddings in index: {self.index.ntotal}")

    def save(self) -> None:
        if self.index is None:
            raise ValueError("Cannot save FAISS store before an index has been built.")

        faiss_path = os.path.join(self.persist_dir, "faiss_index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        faiss.write_index(self.index, faiss_path)
        with open(meta_path, "wb") as file:
            pickle.dump(self.metadata, file)
        print(f"[INFO] FAISS index saved to {faiss_path} and metadata saved to {meta_path}.")

    def load(self) -> None:
        faiss_path = os.path.join(self.persist_dir, "faiss_index")
        meta_path = os.path.join(self.persist_dir, "metadata.pkl")
        self.index = faiss.read_index(faiss_path)
        with open(meta_path, "rb") as file:
            self.metadata = pickle.load(file)
        print(f"[INFO] FAISS index loaded from {faiss_path} and metadata loaded from {meta_path}.")

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> list[dict[str, Any]]:
        if self.index is None:
            raise ValueError("FAISS index is not loaded or built.")

        distances, indexes = self.index.search(query_embedding, top_k)
        results = []
        for idx, distance in zip(indexes[0], distances[0]):
            meta = self.metadata[idx] if 0 <= idx < len(self.metadata) else None
            results.append({"index": int(idx), "metadata": meta, "distance": float(distance)})
        return results

    def query(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        query_embedding = self.embedding_model.encode([query]).astype("float32")
        return self.search(query_embedding, top_k)

