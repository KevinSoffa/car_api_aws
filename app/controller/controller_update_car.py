from app.service.service_update_car import service_update_car
from app.models.car_dto_updated import CarUpdateDTO
from fastapi import APIRouter


router_update_car = APIRouter(tags=["Cars"])

@router_update_car.patch(
    "/v1/cars/{car_id}",
    summary="Atualizar carro por ID",
    description="Atualiza parcialmente um carro no DynamoDB."
)
def update_car(car_id: str, dto: CarUpdateDTO):
    return service_update_car(car_id, dto)
