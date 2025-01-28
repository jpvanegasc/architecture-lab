from fastapi import FastAPI

from app.articles import router as articles_router
from app.health import router as health_router
from app.users import router as users_router

app = FastAPI()

app.include_router(health_router)
app.include_router(articles_router)
app.include_router(users_router)
