from datetime import datetime

from pydantic import BaseModel


class GenreInSchema(BaseModel):
    name: str


class GenreOutSchema(GenreInSchema):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PageGenreSchema(BaseModel):
    page: int = 1
    limit: int = 100
    genres: list[GenreOutSchema]


class Message(BaseModel):
    message: str
