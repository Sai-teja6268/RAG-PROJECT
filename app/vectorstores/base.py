from abc import ABC, abstractmethod

class BaseVectorStore(ABC):
    @abstractmethod
    def build_from_documents(self, vectors: list[list[float]], metadatas: list[dict]):
        pass
    
    @abstractmethod
    def add_vector(self, vector: list[float], metadata: dict):
        pass

    @abstractmethod
    def search(self, query_vector: list[float], top_k: int) -> list[dict]:
        pass
    