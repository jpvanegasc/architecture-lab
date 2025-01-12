import logging
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.config import settings

logger = logging.getLogger(__name__)


engine = create_engine(settings.database_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()


def db_session() -> Session:
    """Database session generator"""
    try:
        db: Session = SessionLocal()
        yield db
    except Exception:
        logger.critical("DB is down", exc_info=True)
        raise
    finally:
        db.close()


DatabaseSession = Annotated[Session, Depends(db_session)]
