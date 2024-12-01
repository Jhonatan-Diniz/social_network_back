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
