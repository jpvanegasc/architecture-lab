from fastapi import APIRouter

router = APIRouter(prefix="/articles", tags=["Articles"])


@router.get("")
def get_articles(
    author: str | None = None, favorited: str | None = None, tag: str | None = None
):
    # TODO
    return {
        "message": "Get all articles",
        "author": author,
        "favorited": favorited,
        "tag": tag,
    }


@router.post("")
def create_article():
    # TODO
    return {"message": "Create an article"}


@router.get("/{slug}")
def get_article(slug: str):
    # TODO
    return {"message": f"Get article {slug}"}


@router.get("/feed")
def get_feed():
    # TODO
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
def get_comments(slug: str):
    # TODO
    return {"message": f"Get comments for article {slug}"}


@router.delete("/{slug}/comments/{comment_id}")
def delete_comment(slug: str, comment_id: int):
    # TODO
    return {"message": f"Delete comment {comment_id} for article {slug}"}


@router.delete("/{slug}")
def delete_article(slug: str):
    # TODO
    return {"message": f"Delete article {slug}"}
