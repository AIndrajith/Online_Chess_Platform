from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:12378Av@##$@localhost:3306/chess_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind=engine,
)