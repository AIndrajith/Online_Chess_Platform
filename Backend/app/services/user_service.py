# create user

from sqlalchemy.orm import Session
from Backend.app.models.user import User
from Backend.app.services.security import hash_password

def create_user(db: Session, username:str, password: str) -> User:
    hashed_password = hash_password(password)

    user = User(
        username = username,
        password = hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user