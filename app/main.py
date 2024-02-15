#~/movie_service/app/main.py
from app.api.models.asegurado import Asegurado
from fastapi import FastAPI, HTTPException
from typing import List
from app.api.routes.route import router

app = FastAPI()

app.include_router(router)