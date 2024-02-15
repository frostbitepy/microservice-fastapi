from app.api.models import Movie
from bson import ObjectId


async def insert_movie(db, movie: Movie):
    result = await db.movies.insert_one(movie.dict())
    return result.inserted_id

async def get_movie_by_id(db, movie_id: str):
    movie = await db.movies.find_one({"_id": ObjectId(movie_id)})
    return movie

async def delete_movie(db, movie_id: str):
    result = await db.movies.delete_one({"_id": ObjectId(movie_id)})
    return result.deleted_count

async def get_all_movies(db):
    movies = []
    for movie in db.movies.find():
        movies.append(movie)
    return movies

async def update_movie(db, movie_id: str, movie: Movie):
    movie = movie.dict()
    result = await db.movies.update_one({"_id": ObjectId(movie_id)}, {"$set": movie})
    return result.modified_count