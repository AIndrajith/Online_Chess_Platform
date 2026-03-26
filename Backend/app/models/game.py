from sqlalchemy import Column, Integer, String, ForeignKey
from Backend.app.database.base import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)

    # who created the game
    creater_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # players (role-based)
    white_player_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    black_player_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # game state
    fen = Column(String(255), nullable=False) # Forsyth-Edwards Notation
    # FEN = standard way to represent a chess position as a single string

    # game status
    status = Column(String(50), nullable=False)