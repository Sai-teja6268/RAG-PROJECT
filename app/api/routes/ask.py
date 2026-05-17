from fastapi import APIRouter

from app.api.schemas.request import AskRequest
from app.api.schemas.response import AskResponse
from app.services.rag_service import RagService

router = APIRouter(prefix="/ask", tags=["rag"])


@router.post("", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    result = RagService().ask(request.question, top_k=request.top_k)
    return AskResponse(**result)

