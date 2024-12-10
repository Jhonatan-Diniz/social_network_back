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
async def create_post(
        request: PostCreate,
        current_user: Annotated[UserModel, Depends(get_current_user)]
        ):
    print(current_user)
    print(request)
    post_service = PostService()
    post = await post_service.create_post(
            user=current_user,
            msg=request.message
            )

    return {'Post': post}


@router.get('/get_posts')
async def get_posts():
    post_service = PostService()
    posts = await post_service.get_all_posts()
    return posts
