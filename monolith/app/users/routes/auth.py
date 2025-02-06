from fastapi import APIRouter, HTTPException, status

from app.db import DatabaseSession
from app.users.models import User
from app.users.schemas import SingleUserCreate, SingleUserResponse, UserOut

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
    return SingleUserResponse(user=UserOut.model_validate(user))


@router.post("/users/login")
def login():
    return {"message": "Login"}


@router.post("/user")
def get_current_user():
    return {"message": "Get current user"}


@router.put("/user")
def update_user():
    return {"message": "Update user"}
