from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base
from app.security import get_password_hash


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    email: Mapped[str] = mapped_column(unique=True)
    bio: Mapped[str] = mapped_column(nullable=True)
    image_url: Mapped[str] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )

    articles = relationship("Article", back_populates="author")

    @classmethod
    def safe_create(cls, **kwargs):
        raw_password = kwargs.pop("password")
        if not raw_password:
            raise ValueError("password required")
        password = get_password_hash(raw_password)
        user = cls(**kwargs, password=password)
        return user


class Follower(Base):
    __tablename__ = "followers"

    follower_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    followed_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
