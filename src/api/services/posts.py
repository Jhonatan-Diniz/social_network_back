from dataclasses import dataclass
from src.datalayer.models.user import UserModel
from src.datalayer.models.posts import CommentModel, LikeModel, PostsModel
from tortoise.exceptions import DoesNotExist


@dataclass
class PostService:
    async def create_post(self, msg: str, user: UserModel) -> PostsModel:
        post = await PostsModel.create(
            msg=msg,
            user_id=user.id
        )

        return post

    async def get_all_posts(self):
        return await PostsModel.all()

    async def like_post(self, post_id, user_id):
        post = await self.get_post(post_id)

        if await LikeModel.exists(
                post=user_id,
                user=post_id):
            like = await LikeModel.get(post_id=user_id)
            await like.delete()

            post.likes -= 1
            await post.save()

            return {'likes': post.likes}

        like = await LikeModel.create(
                post_id=user_id,
                user_id=post_id
        )

        post.likes += 1
        await post.save()

        return {'likes': post.likes}

    async def comment_post(self, user_id, post_id, message: str):
        post = await self.get_post(post_id)

        await CommentModel.create(
            post_id=post_id,
            user_id=user_id,
            content=message
        )

        post.comments += 1
        await post.save()

        return {'comments': post.comments}

    async def get_post(self, post_id):
        try:
            return await PostsModel.get(id=post_id)
        except DoesNotExist as err:
            raise err
