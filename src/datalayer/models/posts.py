from tortoise.models import Model
from tortoise import fields


class PostsModel(Model):
    id = fields.IntField(primary_key=True)
    msg = fields.CharField(max_length=200)
    created = fields.DatetimeField(null=True, auto_now_add=True)
    user = fields.ForeignKeyField(
            'models.UserModel',
            related_name='user_posts'
            )
    likes = fields.IntField(default=0)
    comments = fields.IntField(default=0)


class LikeModel(Model):
    user = fields.ForeignKeyField(
            'models.UserModel',
            related_name='user_likes'
    )
    post = fields.ForeignKeyField(
            'models.PostsModel',
            related_name='posts_likes'
    )


class CommentModel(Model):
    user = fields.ForeignKeyField(
            'models.UserModel',
            related_name='user_comment'
            )
    post = fields.ForeignKeyField(
            'models.PostsModel',
            related_name='post_comment'
            )
    content = fields.TextField()
