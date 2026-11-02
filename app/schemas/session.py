from typing import Annotated

from pydantic import BaseModel, StringConstraints


class SessionCreate(BaseModel):
    game_id: int
    player_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class SessionResponse(BaseModel):
    id: int
    game_id: int
    player_name: str
