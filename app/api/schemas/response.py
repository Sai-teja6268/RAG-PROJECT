from typing import Any

try:
    from pydantic import BaseModel
except ImportError:
    BaseModel = object


class AskResponse(BaseModel):
    answer: str
    contexts: list[dict[str, Any]]
    citations: list[dict[str, Any]]
    confidence: float


class IngestResponse(BaseModel):
    documents: int
    persist_dir: str


class HealthResponse(BaseModel):
    status: str

