from fastapi import APIRouter, Depends
from http import HTTPStatus
from src.api.services.user import UserService
from typing import Annotated
from src.api.auth import get_current_user
from src.datalayer.models.user import UserModel
from src.api.schemas.user import (
    RegisterUser,
    LoginUser,
    ImageUser
)

router = APIRouter(
        prefix='/users',
        tags=['users'],
        responses={404: {"description": "Not found"}}
        )


@router.post("/register")
async def register(request: RegisterUser):
    user_service = UserService()
    if not await user_service.validateForm(request):
        return {
                'status': HTTPStatus.NOT_ACCEPTABLE,
                'msg': 'The email is not valid'
        }

    user = await user_service.registerUser(
        name=request.name,
        email=request.email,
        password=request.password
        )
    return user


@router.post('/login')
async def login(request: LoginUser):
    user_service = UserService()
    user_infos = await user_service.loginUser(
            email=request.email,
            password=request.password
            )

    return user_infos


@router.get('/get_all')
async def getAll():
    user_service = UserService()
    all_users = await user_service.getAllUsers()

    return all_users


@router.get("/{user_id}")
async def getUser(user_id: int):
    user_service = UserService()
    user = await user_service.get_user(user_id)
    if user is None:
        return {
                'status': HTTPStatus.NOT_FOUND,
                'msg': 'This user dont exist!'
                }

    user_data = {
            'user_id': user.id,
            'name': user.name,
            'email': user.email
            }

    return user_data


@router.post("/set_image")
async def set_image(
        request: ImageUser,
        current_user: Annotated[UserModel, Depends(get_current_user)]
        ):
    user_service = UserService()
    data = {
        'user': current_user,
        'image': request.image
    }
    set_image = await user_service.set_image(data)
    return set_image
