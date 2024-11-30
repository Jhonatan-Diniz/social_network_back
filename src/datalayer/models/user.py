from tortoise.models import Model
from tortoise import fields


class UserModel(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    email = fields.CharField(max_length=50)
    password = fields.CharField(max_length=70)
    created = fields.DatetimeField(auto_now_add=True)
