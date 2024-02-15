#~/movie_service/app/main.py
from fastapi import FastAPI
from app.api.movies import movies
from app.api.db import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.db = await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection(app.state.db)

app.include_router(movies)