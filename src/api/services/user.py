from dataclasses import dataclass
from src.datalayer.models.user import UserModel
from http import HTTPStatus


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

        user = await UserModel.create(
                name=name,
                email=email,
                password=password
        )

        return user

    async def loginUser(self):
        ...

    async def userExistsByName(self, username) -> bool:
        # Checks the user name at database, returns a boolean ValueError
        return await UserModel.exists(name=username)

    async def userExistsByEmail(self, email) -> bool:
        # Checks the user email at database, returns a boolean value
        return await UserModel.exists(email=email)

    async def userExistsById(self, user_id) -> bool:
        # Checks the user id at database, returns a boolean value
        return await UserModel.exists(id=user_id)
