from fastapi import Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from app.db import DatabaseSession
from app.security import decode_access_token
from app.users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def get_current_user(
    db: DatabaseSession,
    token: str = Header(None, alias="Authorization"),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # FIXME:
        token = token[6:]
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except InvalidTokenError as ex:
        raise credentials_exception from ex
    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        raise credentials_exception
    return user
