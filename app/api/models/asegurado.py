from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Asegurado(BaseModel):
    id: str = Field(alias="$oid")
    seccion: int = Field(alias="$numberInt")
    poliza: int = Field(alias="$numberInt")
    endoso: int = Field(alias="$numberInt")
    certificado: int = Field(alias="$numberInt")
    emision: datetime = Field(alias="$date")
    asegurado: str
    nacimiento: datetime = Field(alias="$date")
    documento: int = Field(alias="$numberInt")
    capital: int = Field(alias="$numberInt")
    tipo: Optional[float] = Field(alias="$numberDouble")
    plazo: Optional[float] = Field(alias="$numberDouble")
    desde: datetime = Field(alias="$date")
    cancelacion: datetime = Field(alias="$date")
    premio: int = Field(alias="$numberInt")
    solicitud: Optional[float] = Field(alias="$numberDouble")

    class Config:
        allow_population_by_field_name = True