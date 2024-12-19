from pydantic import BaseModel


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class ImageUser(BaseModel):
    image: str
