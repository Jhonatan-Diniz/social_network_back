from typing import Annotated
from fastapi import APIRouter, Depends
from src.api.auth import get_current_user
from src.datalayer.models.user import UserModel
from src.api.services.posts import PostService
from src.api.schemas.posts import (
    PostCreate,
)

router = APIRouter(
        prefix='/posts',
        tags=['users'],
        responses={404: {"description": "Not found"}}
        )


@router.post("/create_post")
async def register(
        request: PostCreate,
        current_user: Annotated[UserModel, Depends(get_current_user)]
        ):
    post_service = PostService()
    post = await post_service.create_post(
            user=current_user,
            msg=request.message
            )

    return {'Post': post}
