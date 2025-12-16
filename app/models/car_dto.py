from pydantic import BaseModel


class CarDTO(BaseModel):
    nome: str
    marca: str
    modelo: str
    ano: int
    valor: float
