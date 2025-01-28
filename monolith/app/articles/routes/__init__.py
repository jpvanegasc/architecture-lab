"""
It is not ideal to separate a small module into multiple files. Still, given that there
are two top-level resources (articles and tags), this was the sensible approach to avoid
having a separate tags "app" or multiple routers in the same file.
"""

from fastapi import APIRouter

from app.articles.routes.articles import router as articles_router
from app.articles.routes.tags import router as tags_router

router = APIRouter()
router.include_router(articles_router)
router.include_router(tags_router)
