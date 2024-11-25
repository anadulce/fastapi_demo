from http import HTTPStatus

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy import select
from sqlalchemy.exc import (
    IntegrityError,
)
from sqlalchemy.orm import Session

from src.database import get_session
from src.models import Genre
from src.routers.schema import (
    GenreInSchema,
    GenreOutSchema,
    Message,
    PageGenreSchema,
)

router = APIRouter(prefix='/genre', tags=['genres'])


@router.post(
    '/',
    status_code=HTTPStatus.CREATED,
    response_model=GenreOutSchema,
)
def create_genre(
    genre: GenreInSchema,
    session: Session = Depends(get_session),
):
    try:
        db_genre = Genre(**genre.model_dump())
        session.add(db_genre)
        session.commit()
        session.refresh(db_genre)
        return db_genre
    except IntegrityError:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST,
            detail='Genre already exists',
        )


# @router.get(
#     '/',
#     status_code=HTTPStatus.OK,
#     response_model=list[GenreOutSchema],
# )
# def read_genre(
#     session: Session = Depends(get_session),
# ):
#     genres = session.execute(select(Genre)).scalars().all()
#     return genres


@router.get('/', response_model=PageGenreSchema)
def read_genre(
    page: int = 1,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    genres = session.scalars(
        select(Genre).offset((page - 1) * limit).limit(limit)
    ).all()

    return {
        'page': page,
        'limit': limit,
        'genres': genres,
    }


@router.get('/{id}/', response_model=GenreOutSchema)
def get_genre(
    id: int,
    session: Session = Depends(get_session),
):
    if genre := session.scalars(
        select(Genre).where(Genre.id == id)
    ).one_or_none():
        return genre

    raise HTTPException(
        HTTPStatus.BAD_REQUEST,
        detail='Genre not found',
    )


@router.put(
    '/{id}/',
    status_code=HTTPStatus.OK,
    response_model=GenreOutSchema,
)
def update_genre(
    id: int,
    genre_to_update: GenreInSchema,
    session: Session = Depends(get_session),
):
    if db_genre := session.scalars(
        select(Genre).where(Genre.id == id)
    ).one_or_none():
        try:
            for (
                attr,
                value,
            ) in genre_to_update.dict(exclude_unset=True).items():
                setattr(db_genre, attr, value)

            session.add(db_genre)
            session.commit()
            session.refresh(db_genre)
            return db_genre
        except IntegrityError:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                detail='Genre already exists',
            )
    raise HTTPException(
        HTTPStatus.BAD_REQUEST,
        detail='Genre not found',
    )


@router.patch(
    '/{id}/',
    status_code=HTTPStatus.OK,
    response_model=GenreOutSchema,
)
def partial_update_genre(
    id: int,
    genre_to_update: GenreInSchema,
    session: Session = Depends(get_session),
):
    if db_genre := session.scalars(
        select(Genre).where(Genre.id == id)
    ).one_or_none():
        try:
            for (
                attr,
                value,
            ) in genre_to_update.dict(exclude_unset=True).items():
                setattr(db_genre, attr, value)

            session.add(db_genre)
            session.commit()
            session.refresh(db_genre)
            return db_genre
        except IntegrityError:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                detail='Genre already exists',
            )
    raise HTTPException(
        HTTPStatus.BAD_REQUEST,
        detail='Genre not found',
    )


@router.delete(
    '/{id}/',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def delete_genre(
    id: int,
    session: Session = Depends(get_session),
):
    if db_genre := session.scalars(
        select(Genre).where(Genre.id == id)
    ).one_or_none():
        session.delete(db_genre)
        session.commit()
        return {'message': 'Genre deleted'}
    raise HTTPException(
        HTTPStatus.BAD_REQUEST,
        detail='Genre not found',
    )
