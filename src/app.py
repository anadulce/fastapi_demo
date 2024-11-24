from typing import Annotated


from http import HTTPStatus
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Query

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import get_session
from src.routers.genre import router as genre_router
from src.routers.movie import router as movie_router


app = FastAPI()


app.include_router(genre_router)
app.include_router(movie_router)
