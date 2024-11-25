from fastapi import FastAPI

from src.routers.genre import router as genre_router

app = FastAPI()


app.include_router(genre_router)
