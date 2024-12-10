from fastapi import APIRouter
from src.api.services.user import UserService
from src.api.schemas.user import (
    RegisterUser,
    LoginUser
)

router = APIRouter(
        prefix='/users',
        tags=['users'],
        responses={404: {"description": "Not found"}}
        )


@router.post("/register")
async def register(request: RegisterUser):
    print(request)
    user_service = UserService()
    user = await user_service.registerUser(
        name=request.name,
        email=request.email,
        password=request.password
        )
    return user


@router.post('/login')
async def login(request: LoginUser):
    user_service = UserService()
    access_token = await user_service.loginUser(
            email=request.email,
            password=request.password
            )

    return access_token


@router.get('/get_all')
async def getAll():
    user_service = UserService()
    all_users = await user_service.getAllUsers()

    return all_users
