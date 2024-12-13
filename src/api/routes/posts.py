from typing import Annotated
from fastapi import APIRouter, Depends
from src.api.auth import get_current_user
from src.datalayer.models.user import UserModel
from src.api.services.posts import PostService
from src.api.schemas.posts import (
    PostComment,
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
    post_service = PostService()
    post = await post_service.create_post(
            user=current_user,
            msg=request.message
            )

    return {'Post': post}


@router.post('/{post_id}/like')
async def like(
        post_id: int,
        current_user: Annotated[UserModel, Depends(get_current_user)]
        ):
    post_service = PostService()
    likes_post = await post_service.like_post(
            post_id=post_id,
            user_id=current_user.id
    )

    return likes_post


@router.post('/{post_id}/comment')
async def comment(
        post_id: int,
        comment_msg: PostComment,
        current_user: Annotated[UserModel, Depends(get_current_user)]
        ):
    post_service = PostService()

    comment_post = await post_service.comment_post(
        user_id=current_user.id,
        post_id=post_id,
        message=comment_msg.message
    )

    return comment_post


@router.get('/{user_id}/')
async def get_posts_from_user(
        user_id: int
        ):
    post_service = PostService()

    posts_list = await post_service.get_posts_by_user(
            user_id=user_id
            )
    return posts_list


@router.get('/get_posts')
async def get_posts():
    post_service = PostService()
    posts = await post_service.get_all_posts()
    return posts
