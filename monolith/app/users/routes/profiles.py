from fastapi import APIRouter

router = APIRouter(tags=["Profiles"])


@router.get("/profiles/celeb_{username}")
def get_celebrity_profile(username: str):
    return {"message": f"Get celebrity profile: {username}"}


@router.post("/profiles/celeb_{username}/follow")
def follow_celebrity(username: str):
    return {"message": f"Follow celebrity: {username}"}


@router.delete("/profiles/celeb_{username}/follow")
def unfollow_celebrity(username: str):
    return {"message": f"Unfollow celebrity: {username}"}
