from pydantic import BaseModel

from app.schemas import BaseAPIResponse


class UserOut(BaseAPIResponse):
    id: int
    username: str
    email: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class SingleUserResponse(BaseAPIResponse):
    user: UserOut


class SingleUserCreate(BaseModel):
    user: UserCreate
