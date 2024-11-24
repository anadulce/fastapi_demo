from datetime import datetime
from fastapi import Query


from pydantic import BaseModel

class GenreInSchema(BaseModel):
    name: str


class GenreOutSchema(GenreInSchema):
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class GenreDBSchema(GenreOutSchema):
    id: int
    class Config:
        from_attributes = True

class GenreUpdateSchema(BaseModel):
    name: str | None = None


class MovieInSchema(BaseModel):
    name: str
    director: str
    year: int
    genre: int


class MovieOutSchema(MovieInSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    genre: GenreOutSchema

    class Config:
        from_attributes = True

class MovieUpdateSchema(BaseModel):
    name: str | None = None
    director: str | None = None
    year: int | None = None
    genre: int | None = None
    id: int | None = None
    genre: int | None = None

class MovieDBSchema(MovieOutSchema):
    id: int
    class Config:
        from_attributes = True

class PageGenreSchema(BaseModel):
    offset: int = 0
    limit: int = 100
    genres: list[GenreOutSchema]

class Message(BaseModel):
    message: str

