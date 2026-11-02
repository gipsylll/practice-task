from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.session import SessionCreate, SessionResponse
from app.services.session import SessionService, get_session_service

sessions_router = APIRouter(prefix="/sessions", tags=["sessions"])


@sessions_router.post(
    "",
    response_model=SessionResponse,
    status_code=status.HTTP_200_OK,
)
def create_session(
    payload: SessionCreate,
    service: Annotated[SessionService, Depends(get_session_service)],
) -> SessionResponse:
    return service.create_session(payload)
