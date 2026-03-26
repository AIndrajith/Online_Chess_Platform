from sqlalchemy.orm import Session
from Backend.app.models.game import Game

# starndard starting FEN
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def create_game(db: Session, user_id: int) -> Game:
    game = Game(
        creater_id=user_id,
        white_player_id=user_id,    # creater gets white (simple rule)
        black_player_id=None,
        fen=STARTING_FEN,
        status="waiting"
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    return game

def join_game(db: Session, game_id: int, user_id: int) -> Game:
    game = db.query(Game).filter(Game.id == game_id).first()

    # basic validations
    if not game:
        raise Exception("Game not found")

    if game.black_player_id is not None:
        raise Exception("Game already has two players")

    if game.white_player_id == user_id:
        raise Exception("Creater cannot join as second player")

    # assign second player
    game.black_player_id = user_id
    game.status = "in_progress"

    db.commit()
    db.refresh(game)

    return game