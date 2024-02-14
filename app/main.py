#~/movie_service/app/main.py
from .api.models import Movie
from fastapi import FastAPI, HTTPException
from typing import List
from app.api.movies import movies

app = FastAPI()

app.include_router(movies)