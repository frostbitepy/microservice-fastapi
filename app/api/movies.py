from fastapi import Header, APIRouter, HTTPException
from typing import List
from app.api.models import Movie
from app.api import db_manager


movies = APIRouter()


@movies.get('/', response_model=List[Movie])
async def index():
    return await db_manager.get_all_movies()


@movies.post('/', status_code=201)
async def add_movie(payload: MovieIn):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) -1}


@movies.put('/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")


@movies.delete('/{id}')
async def delete_movie(id: int):
    movies_length = len(fake_movie_db)
    if 0 <= id <= movies_length:
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404, detail="Movie with given id not found")