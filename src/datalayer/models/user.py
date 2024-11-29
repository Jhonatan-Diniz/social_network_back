from tortoise.models import Model
from tortoise import fields


class UserModel(Model):
    # Database model to users profile
    id = fields.IntField(primary_key=True)
    name = fields.TextField(max_length=50)
    email = fields.CharField(max_length=50)
    # hashad password
    password = fields.CharField(max_length=70)
    created = fields.DatetimeField(auto_now_add=True)

    def getUserInfo(self):
        # This return the users information of name and email
        user_info = {
            'name': self.name,
            'email': self.email,
        }
        return user_info
