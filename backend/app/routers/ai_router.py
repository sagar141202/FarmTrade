from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.middleware.auth_middleware import get_current_user
from app.services.groq_service import negotiation_coach

router = APIRouter(prefix="/ai", tags=["AI"])


class NegotiationRequest(BaseModel):

    question: str
    language: str = "English"


@router.post("/negotiation-coach")
def ai_negotiation(
    data: NegotiationRequest,
    user=Depends(get_current_user)
):

    response = negotiation_coach(
        data.question,
        data.language
    )

    return {
        "ai_response": response
    }