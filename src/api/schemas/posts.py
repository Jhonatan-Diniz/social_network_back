from pydantic import BaseModel


class PostCreate(BaseModel):
    message: str
