from app.service.service_get_car import service_get_car
from fastapi import APIRouter


router_get_car = APIRouter(tags=["Cars"])

@router_get_car.get(
    "/v1/cars/{car_id}",
    summary="Buscar carro por ID",
    description="Retorna os dados de um carro usando seu ID."
)
def get_car(car_id: str):
    return service_get_car(car_id)
