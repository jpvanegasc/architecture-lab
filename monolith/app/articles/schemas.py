from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, Field, field_validator

from app.schemas import BaseAPIResponse


class ArticleOut(BaseAPIResponse):
    title: str
    slug: str
    created_at: Annotated[datetime, Field(serialization_alias="createdAt")]
    updated_at: Annotated[datetime, Field(serialization_alias="updatedAt")]
    description: str
    tag_list: Annotated[list[str], Field(serialization_alias="tagList")]
    author: str
    favorited: Optional[bool] = None  # TODO: verify if this is correct
    favorites_count: Annotated[
        Optional[int], Field(None, serialization_alias="favoritesCount")
    ]

    @field_validator("tag_list", mode="before")
    @classmethod
    def validate_tag_list(cls, value):
        if not value:
            return []
        return [tag.tag for tag in value]

    @field_validator("author", mode="before")
    @classmethod
    def validate_author(cls, value):
        return value.username


class ArticleCreate(BaseModel):
    title: str
    description: str
    body: str
    tag_list: list[str]


class ListArticlesResponse(BaseModel):
    articles: list[ArticleOut]
    articles_count: Annotated[int, Field(serialization_alias="articlesCount")]


class SingleArticleResponse(BaseModel):
    article: ArticleOut


class SingleArticleCreate(BaseModel):
    article: ArticleCreate


class CommentOut(BaseAPIResponse):
    id: int
    body: str
    created_at: Annotated[datetime, Field(serialization_alias="createdAt")]
    updated_at: Annotated[datetime, Field(serialization_alias="updatedAt")]
    author: str


class ListCommentsResponse(BaseModel):
    comments: list[CommentOut]
    comments_count: Annotated[int, Field(serialization_alias="commentsCount")]
