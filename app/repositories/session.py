import threading

from app.repositories.base import SessionRepositoryProtocol
from app.schemas.session import SessionResponse


class InMemorySessionRepository(SessionRepositoryProtocol):
    def __init__(self) -> None:
        self._sessions: list[SessionResponse] = []
        self._lock = threading.Lock()

    def create(self, game_id: int, player_name: str) -> SessionResponse:
        with self._lock:
            session = SessionResponse(
                id=len(self._sessions) + 1,
                game_id=game_id,
                player_name=player_name,
            )
            self._sessions.append(session)
            return session


session_repository = InMemorySessionRepository()


def get_session_repository() -> InMemorySessionRepository:
    return session_repository
