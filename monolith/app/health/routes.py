from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from app.db import DatabaseSession

router = APIRouter()


@router.get("/health/db")
def health(db: DatabaseSession):
    try:
        db.execute(text("SELECT 1"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database is down: {e}") from e
    return {"status": "ok"}
