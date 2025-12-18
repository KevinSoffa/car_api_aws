from app.service.service_create_car import service_create_car
from app.models.car_dto import CarDTO
from fastapi import APIRouter, status, Depends
from app.security.dependencies import get_current_user


router_create_car = APIRouter(tags=["Cars"])

@router_create_car.post(
    "/v1/cars",
    status_code=status.HTTP_201_CREATED,
    summary="Criar um novo carro",
    description="Cadastra um novo carro no DynamoDB [ AWS ].",
    response_description="Carro criado com sucesso"
)

def create_car(
    dto: CarDTO,
    user=Depends(get_current_user)
):
    return service_create_car(dto)

