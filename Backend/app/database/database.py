from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from Backend.app.database.base import Base
from urllib.parse import quote_plus

password = quote_plus("12378Av@##$")
DATABASE_URL = f"mysql+mysqlconnector://root:{password}@localhost:3306/chess_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind=engine,
)

def init_db():          # tables are created when only init_db() is called
    import Backend.app.models
    Base.metadata.create_all(bind=engine) # -> create tables only if they do not already exist.