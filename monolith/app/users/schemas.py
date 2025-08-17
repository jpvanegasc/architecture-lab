from pydantic import BaseModel, EmailStr

from app.schemas import BaseAPIResponse


class UserLoginIn(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseAPIResponse):
    username: str
    email: str
    bio: str | None
    image: str | None
    token: str


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class SingleUserLogin(BaseModel):
    user: UserLoginIn


class SingleUserResponse(BaseAPIResponse):
    user: UserOut


class SingleUserCreate(BaseModel):
    user: UserCreate
