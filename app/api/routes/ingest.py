from fastapi import APIRouter

from app.api.schemas.request import IngestRequest
from app.api.schemas.response import IngestResponse
from app.core.config import settings
from app.services.ingestion_service import IngestionService

router = APIRouter(prefix="/ingest", tags=["ingestion"])


@router.post("", response_model=IngestResponse)
def ingest(request: IngestRequest) -> IngestResponse:
    result = IngestionService().ingest(request.data_dir or settings.data_dir)
    return IngestResponse(**result)

