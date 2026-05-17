try:
    from pydantic import BaseModel
except ImportError:
    BaseModel = object


class AskRequest(BaseModel):
    question: str
    top_k: int | None = None


class IngestRequest(BaseModel):
    data_dir: str | None = None

