from dataclasses import dataclass
from src.datalayer.models.user import UserModel
from http import HTTPStatus
from src.api.auth import (
    create_access_token,
    get_password_hash,
    verify_password
)


@dataclass
class UserService:
    async def registerUser(
            self,
            name: str,
            email: str,
            password: str) -> HTTPStatus | UserModel:

        if (
            await self.userExistsByName(name) or
            await self.userExistsByEmail(email)
        ):
            return HTTPStatus.CONFLICT

        hash_password = get_password_hash(password)

        user = await UserModel.create(
                name=name,
                email=email,
                password=hash_password
        )

        return user

    async def loginUser(self, email, password):
        if not await self.userExistsByEmail(email):
            return {
                    'msg': 'Email not found on database',
                    'status': HTTPStatus.NOT_FOUND
            }
        # Get the user on database
        user = await UserModel.get(email=email)

        # Verify the passwords corresponds
        if not verify_password(password, user.password):
            return {
                    'msg': 'Wrong Password',
                    'status': HTTPStatus.NOT_FOUND
            }

        ACCESS_TOKEN = create_access_token(data={'sub': user.email})
        return ACCESS_TOKEN

    async def get_user(self, data):
        user = None
        if await self.userExistsById(data):
            user = await UserModel.get(id=data)
        if await self.userExistsByName(data):
            user = await UserModel.get(name=data)
        if await self.userExistsByEmail(data):
            user = await UserModel.get(email=data)

        return user

    async def userExistsByName(self, username) -> bool:
        # Checks the user name at database, returns a boolean ValueError
        return await UserModel.exists(name=username)

    async def userExistsByEmail(self, email) -> bool:
        # Checks the user email at database, returns a boolean value
        return await UserModel.exists(email=email)

    async def userExistsById(self, user_id) -> bool:
        # Checks the user id at database, returns a boolean value
        return await UserModel.exists(id=user_id)
