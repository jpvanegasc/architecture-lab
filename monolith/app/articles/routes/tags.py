from fastapi import APIRouter

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("")
def get_tags():
    return {"message": "Get all tags"}
