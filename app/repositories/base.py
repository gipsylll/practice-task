from typing import Protocol

from app.schemas.session import SessionResponse


class SessionRepositoryProtocol(Protocol):
    def create(self, game_id: int, player_name: str) -> SessionResponse: ...
