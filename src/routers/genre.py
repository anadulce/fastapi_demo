from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_session
from src.models import Genre
from src.routers.schema import (
    GenreInSchema,
    GenreOutSchema,
)

router = APIRouter(prefix='/genre', tags=['genres'])


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=GenreOutSchema
)
def create_genre(
    genre: GenreInSchema, session: Session = Depends(get_session)
):
    db_genre = Genre(**genre.model_dump())
    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)

    return db_genre
