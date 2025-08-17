from datetime import timedelta

from fastapi import APIRouter, HTTPException, status

from app.config import settings
from app.db import DatabaseSession
from app.security import create_access_token, verify_password
from app.users.models import User
from app.users.schemas import (
    SingleUserCreate,
    SingleUserLogin,
    SingleUserResponse,
    UserOut,
)

router = APIRouter(tags=["Auth"])


@router.post(
    "/users",
    response_model=SingleUserResponse,
    status_code=status.HTTP_201_CREATED,
    description="Register a new user",
    responses={status.HTTP_201_CREATED: {"description": "Return the created user"}},
)
def register(db: DatabaseSession, create_payload: SingleUserCreate):
    user_create = create_payload.user
    if db.query(User).filter(User.username == user_create.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    if db.query(User).filter(User.email == user_create.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )
    user = User.safe_create(**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.id, access_token_expires)

    return SingleUserResponse(
        user=UserOut(
            username=user.username,
            email=user.email,
            bio=user.bio,
            image=user.image_url,
            token=token,
        )
    )


@router.post(
    "/users/login",
    response_model=SingleUserResponse,
    status_code=status.HTTP_200_OK,
    description="Login",
    responses={status.HTTP_200_OK: {"description": "Return the access token"}},
)
def login(db: DatabaseSession, form_data: SingleUserLogin):
    user = db.query(User).filter(User.email == form_data.user.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad username or password"
        )
    if not verify_password(form_data.user.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad username or password"
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.id, access_token_expires)

    return SingleUserResponse(
        user=UserOut(
            username=user.username,
            email=user.email,
            bio=user.bio,
            image=user.image_url,
            token=token,
        )
    )


@router.post("/user")
def get_current_user():
    return {"message": "Get current user"}


@router.put("/user")
def update_user():
    return {"message": "Update user"}
