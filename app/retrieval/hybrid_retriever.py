from app.retrieval.dense_retriever import DenseRetriever
from app.retrieval.sparse_retriever import SparseRetriever
from app.retrieval.fusion import reciprocal_rank_fusion
from app.ingestion.loader import load_all_documents
from app.ingestion.chunker import chunk_documents
from app.vectorstores.faiss_store import FaissVectorStore
from app.core.config import Settings

from langchain_core.documents import Document

class HybridRetriever:
    def __init__(self):
        self.sparse_retriever = SparseRetriever()
        self.dense_retriever = DenseRetriever()
        
        # Load existing chunks from FAISS metadata to build BM25
        # This avoids re-reading and re-embedding documents on every instantiation
        self.chunks = []
        for meta in self.dense_retriever.vector_store.metadata:
            text = meta.get("text", "")
            self.chunks.append(Document(page_content=text, metadata=meta))
            
        if self.chunks:
            self.sparse_retriever.build_index(self.chunks)

    def search(self, query: str, top_k: int = 5):
        sparse_results = self.sparse_retriever.search(query, top_k)
        dense_results = self.dense_retriever.search(query, top_k)
        fused_results = reciprocal_rank_fusion([sparse_results, dense_results])
        return fused_results[:top_k]
