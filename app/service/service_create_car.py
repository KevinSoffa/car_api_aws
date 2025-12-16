from app.repository.repo_create_car import repo_create_car
from fastapi import HTTPException, status
from app.models.car_dto import CarDTO
from app.models.car_dao import CarDAO
import uuid


def service_create_car(dto: CarDTO):

    # REGRA DE NEGÓCIO
    if dto.valor <= 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O valor do carro deve ser maior que 1000"
        )
    

    dao = CarDAO(
        car_id=str(uuid.uuid4()),
        nome=dto.nome,
        marca=dto.marca,
        modelo=dto.modelo,
        ano=dto.ano,
        valor=dto.valor
    )

    return repo_create_car(dao)

