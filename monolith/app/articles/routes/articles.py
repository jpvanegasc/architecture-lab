from fastapi import APIRouter, HTTPException, status

from app.articles.models import Article, ArticleTag, Comment, Tag
from app.articles.schemas import (
    ArticleOut,
    CommentOut,
    ListArticlesResponse,
    ListCommentsResponse,
    SingleArticleResponse,
)
from app.db import DatabaseSession
from app.users.models import User

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.get(
    "",
    response_model=ListArticlesResponse,
    status_code=status.HTTP_200_OK,
    description="Get all articles",
    responses={status.HTTP_200_OK: {"description": "Return all articles"}},
)
def get_articles(
    db: DatabaseSession,
    author: str | None = None,
    favorited: str | None = None,
    tag: str | None = None,
):
    query = db.query(Article)

    if author:
        query = query.join(User).filter(User.username == author)
    if favorited:
        query = query.join(User).filter(User.username == favorited)
    if tag:
        query = query.join(ArticleTag).join(Tag).filter(Tag.tag == tag)

    articles = query.all()
    count = query.count()

    return ListArticlesResponse(
        articles=[ArticleOut.model_validate(a) for a in articles], articles_count=count
    )


@router.post("")
def create_article():
    # TODO
    return {"message": "Create an article"}


@router.get(
    "/{slug}",
    response_model=SingleArticleResponse,
    status_code=status.HTTP_200_OK,
    description="Get an article by slug",
    responses={
        status.HTTP_200_OK: {"description": "Return the article"},
        status.HTTP_404_NOT_FOUND: {"description": "Article not found"},
    },
)
def get_article(db: DatabaseSession, slug: str):
    article = db.query(Article).filter(Article.slug == slug).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Article not found"
        )
    return SingleArticleResponse(article=ArticleOut.model_validate(article))


@router.get("/feed")
def get_feed():
    # TODO: same as get_articles but for uses the token to filter the articles
    return {"message": "Get feed"}


@router.put("/{slug}")
def update_article(slug: str):
    # TODO
    return {"message": f"Update article {slug}"}


@router.post("/{slug}/favorite")
def favorite_article(slug: str):
    # TODO
    return {"message": f"Favorite article {slug}"}


@router.delete("/{slug}/favorite")
def unfavorite_article(slug: str):
    # TODO
    return {"message": f"Unfavorite article {slug}"}


@router.post("/{slug}/comments")
def create_comment(slug: str):
    # TODO
    return {"message": f"Create comment for article {slug}"}


@router.get("/{slug}/comments")
def get_comments(db: DatabaseSession, slug: str):
    query = db.query(Comment).join(Article).filter(Article.slug == slug)
    comments = query.all()
    count = query.count()
    return ListCommentsResponse(
        comments=[CommentOut.model_validate(c) for c in comments], comments_count=count
    )


@router.delete("/{slug}/comments/{comment_id}")
def delete_comment(slug: str, comment_id: int):
    # TODO
    return {"message": f"Delete comment {comment_id} for article {slug}"}


@router.delete("/{slug}")
def delete_article(slug: str):
    # TODO
    return {"message": f"Delete article {slug}"}
