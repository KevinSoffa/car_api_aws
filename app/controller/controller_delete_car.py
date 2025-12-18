from app.service.service_delete_car import service_delete_car
from fastapi import APIRouter


router_delete_car = APIRouter(tags=["Cars"])

@router_delete_car.delete(
    "/v1/cars/{car_id}",
    summary="Remover carro por ID",
    description="Apaga um carro existente do DynamoDB [ AWS ]."
)
def delete_car(car_id: str):
    return service_delete_car(car_id)
