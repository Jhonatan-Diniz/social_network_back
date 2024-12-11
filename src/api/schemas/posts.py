from pydantic import BaseModel


class PostCreate(BaseModel):
    message: str


class PostComment(BaseModel):
    message: str
