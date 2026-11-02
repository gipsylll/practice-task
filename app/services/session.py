from app.repositories.base import SessionRepositoryProtocol
from app.repositories.session import get_session_repository
from app.schemas.session import SessionCreate, SessionResponse


class SessionService:
    def __init__(self, repository: SessionRepositoryProtocol) -> None:
        self._repository = repository

    def create_session(self, payload: SessionCreate) -> SessionResponse:
        return self._repository.create(
            game_id=payload.game_id,
            player_name=payload.player_name,
        )


def get_session_service() -> SessionService:
    return SessionService(repository=get_session_repository())
