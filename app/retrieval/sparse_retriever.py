from rank_bm25 import BM25Okapi
from app.vectorstores.faiss_store import FaissVectorStore
from app.services.embedding_service import EmbeddingService

class SparseRetriever:
    """Placeholder for BM25 or keyword retrieval."""

    def __init__(self):
        self.documents = []
        self.tokenized_corpus = []
        self.bm25 = None

    def build_index(self, chunks):
        self.documents = chunks
        self.tokenized_corpus = [chunk.page_content.lower().split() for chunk in chunks]
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        print(f"[DEBUG] Sparse index built for {len(chunks)} chunks.self.bm25: {self.bm25}")
    
    def search(self, query:str, top_k:int = 5):
        """Retrieve documents using BM25"""
        tokenized_query = query.lower().split()
        scores = self.bm25.get_scores(tokenized_query)
        rank_results = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True
        )
        results =[]

        for chunk, score in rank_results[:top_k]:
            results.append({
                "score": float(score),
                "page_content": chunk.page_content,
                "metadata": chunk.metadata
            })
        return results
