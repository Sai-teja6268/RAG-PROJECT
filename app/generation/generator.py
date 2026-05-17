from langchain_groq import ChatGroq
from app.core.config import settings
from app.generation.prompt_builder import promptBuilder
from typing import Any, List

class Generator:
    """Placeholder for LLM-backed answer generation."""

    def __init__(self,model=settings.llm_model,api_key=settings.groq_api_key):
        self.llm = ChatGroq(model_name=model,api_key=api_key)

    def generate(self, query: str, retrieved_chunks: List[Any]) -> str:
        prompt = promptBuilder.build_prompt(query, retrieved_chunks)
        response = self.llm.invoke(prompt)
        return response.content

