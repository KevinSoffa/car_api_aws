from app.service.service_get_car import service_get_car
from app.security.dependencies import get_current_user
from fastapi import APIRouter, Depends


router_get_car = APIRouter(tags=["Cars"])

@router_get_car.get(
    "/v1/cars/{car_id}",
    summary="Buscar carro por ID",
    description="Retorna os dados de um carro usando seu ID."
)
def get_car(car_id: str, user=Depends(get_current_user)):
    return service_get_car(car_id)
