from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Backend.app.database.deps import get_db
from Backend.app.services.game_service import create_game, join_game

router = APIRouter(prefix="/games", tags=["Games"])

@router.post("/create")
def create_game_endpoint(user_id: int, db: Session = Depends(get_db)):
    game = create_game(db, user_id)
    return game

@router.post("/join/{game_id}")
def join_game_endpoint(game_id: int, user_id: int, db: Session = Depends(get_db)):
    game = join_game(db, game_id, user_id)
    return game