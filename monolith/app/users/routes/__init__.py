from fastapi import APIRouter

from app.users.routes.auth import router as auth_router
from app.users.routes.profiles import router as profiles_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(profiles_router)
