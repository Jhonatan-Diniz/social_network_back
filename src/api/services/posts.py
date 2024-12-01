from dataclasses import dataclass
from src.datalayer.models.user import UserModel
from src.datalayer.models.posts import PostsModel


@dataclass
class PostService:
    async def create_post(self, msg: str, user: UserModel) -> PostsModel:
        post = await PostsModel.create(
            msg=msg,
            user=user
        )

        return post
