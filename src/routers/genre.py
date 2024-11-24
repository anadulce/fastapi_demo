from typing import Annotated

from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException, Query

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from src.database import get_session
from src.models import Genre
from src.routers.schema import GenreInSchema, GenreOutSchema, PageGenreSchema, GenreUpdateSchema, Message
from src.crud import create

router = APIRouter(prefix='/genre', tags=['genres'])

@router.post('/', status_code=HTTPStatus.CREATED, response_model=GenreOutSchema)
def create_genre(genre: GenreInSchema, session: Session = Depends(get_session)):
    return create(session, Genre, genre)
    db_genre = Genre(**genre.model_dump())
    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)

    return db_genre


# @router.get('/', status_code=HTTPStatus.OK, response_model=list[GenreOutSchema])
# def read_genre(session: Session = Depends(get_session)):
#     genres = session.execute(select(Genre)).scalars().all() 
#     return genres


@router.get('/', response_model=PageGenreSchema)
def read_genres(page: int = 1, limit: int = 100, session: Session = Depends(get_session)):
    genres = session.scalars(
        select(Genre).offset((page-1)*limit).limit(limit)
    ).all()

    return {"page": page, "limit": limit, "genres": genres}


@router.put('/{id}/', status_code=HTTPStatus.OK, response_model=GenreOutSchema)
def create_genre(id:int, genre_to_update: GenreUpdateSchema, session: Session = Depends(get_session)):
    db_genre = session.execute(select(Genre).where(Genre.id==id)).scalars().one()

    for attr, value in genre_to_update.dict(exclude_unset=True).items():
        setattr(db_genre, attr, value)
    
    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)

    return db_genre

@router.put('/{id}/', status_code=HTTPStatus.OK, response_model=GenreOutSchema)
def update_genre(id:int, genre_to_update: GenreUpdateSchema, session: Session = Depends(get_session)):
    db_genre = session.execute(select(Genre).where(Genre.id==id)).scalars().one()

    for attr, value in genre_to_update.dict(exclude_unset=True).items():
        setattr(db_genre, attr, value)
    
    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)

    return db_genre

@router.delete('/{id}/', status_code=HTTPStatus.OK, response_model=Message)
def delete_genre(id:int, session: Session = Depends(get_session)):
    try:
        db_genre = session.execute(select(Genre).where(Genre.id==id)).scalars().one()
    except NoResultFound:
        return {'message': 'Genre not deleted'}
    session.delete(db_genre)
    session.commit()

    return {'message': 'Genre deleted'}