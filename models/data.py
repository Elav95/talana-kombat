from pydantic import BaseModel, Field
from typing import List

class Player(BaseModel):
    movimientos: List[str] = Field(..., description = "Lista de movimientos")
    golpes: List[str] = Field(..., description = "Lista de golpes")

class Pelea(BaseModel):
    player1: Player = Field(..., description = "Player 1")
    player2: Player = Field(..., description = "Player 2")