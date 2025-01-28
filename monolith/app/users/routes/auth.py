from fastapi import APIRouter

router = APIRouter(tags=["Auth"])


@router.post("/users")
def register():
    return {"message": "Register"}


@router.post("/users/login")
def login():
    return {"message": "Login"}


@router.post("/user")
def get_current_user():
    return {"message": "Get current user"}


@router.put("/user")
def update_user():
    return {"message": "Update user"}
