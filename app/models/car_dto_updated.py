from pydantic import BaseModel
from typing import Optional


class CarUpdateDTO(BaseModel):
    nome: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = None
    valor: Optional[float] = None
