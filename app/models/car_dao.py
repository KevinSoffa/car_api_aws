from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CarDAO:
    car_id: str
    nome: str
    marca: str
    modelo: str
    ano: int
    valor: Decimal

    def __post_init__(self):
        if not isinstance(self.valor, Decimal):
            self.valor = Decimal(str(self.valor))
