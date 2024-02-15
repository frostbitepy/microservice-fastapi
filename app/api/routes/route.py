from fastapi import APIRouter
from app.api.models.asegurado import Asegurado
from app.api.config.database import collection
from app.api.schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


@router.get("/asegurados")
async def get_asegurados():
    asegurados = await collection.find()
    return list_serial(asegurados) 

