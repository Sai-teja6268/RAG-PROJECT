from app.core.config import settings
from app.retrieval.hybrid_retriever import HybridRetriever
from app.generation.generator import Generator


class RagService:
    def __init__(self):
        self.retriever = HybridRetriever()
        self.generator = Generator()

    def ask(self, question: str, top_k: int =5) -> dict:
        retrieved_chunks = self.retriever.search(question, top_k)
        print("retrieved_chunks",retrieved_chunks)
        answer = self.generator.generate(question, retrieved_chunks)
        return {
            "query": question,
            "answer": answer,
            "contexts": (retrieved_chunks),
        }

