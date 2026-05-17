import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from app.core.constants import (
    DATA_DIR,
    DEFAULT_CHUNK_OVERLAP,
    DEFAULT_CHUNK_SIZE,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_TOP_K,
    VECTOR_STORE_DIR,
)

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "rag-project")
    data_dir: Path = Path(os.getenv("DATA_DIR", str(DATA_DIR)))
    vector_store_dir: Path = Path(os.getenv("VECTOR_STORE_DIR", str(VECTOR_STORE_DIR)))
    embedding_model: str = os.getenv("EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL)
    chunk_size: int = int(os.getenv("CHUNK_SIZE", DEFAULT_CHUNK_SIZE))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", DEFAULT_CHUNK_OVERLAP))
    top_k: int = int(os.getenv("TOP_K", DEFAULT_TOP_K))
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    llm_model:str = os.getenv("LLM_MODEL", "llama-3.1-8b-instant")


settings = Settings()

