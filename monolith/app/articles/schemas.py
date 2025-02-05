from typing import Annotated

from pydantic import BaseModel, Field

from app.schemas import BaseAPIResponse


class ArticleOut(BaseAPIResponse):
    title: str
    slug: str
    created_at: Annotated[str, Field(serialization_alias="createdAt")]
    updated_at: Annotated[str, Field(serialization_alias="updatedAt")]
    description: str
    tag_list: Annotated[list[str], Field(serialization_alias="tagList")]
    author: str
    favorited: bool
    favorites_count: Annotated[int, Field(serialization_alias="favoritesCount")]


class ListArticlesResponse(BaseModel):
    articles: list[ArticleOut]
    articles_count: Annotated[int, Field(serialization_alias="articlesCount")]
