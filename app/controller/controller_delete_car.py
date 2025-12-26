from app.service.service_delete_car import service_delete_car
from app.security.dependencies import get_current_user
from fastapi import APIRouter, status, Depends


router_delete_car = APIRouter(tags=["Cars"])

@router_delete_car.delete(
    "/v1/cars/{car_id}",
    summary="Remover carro por ID",
    description="Apaga um carro existente do DynamoDB [ AWS ].",
    status_code=status.HTTP_200_OK
)
def delete_car(car_id: str, user=Depends(get_current_user)):
    return service_delete_car(car_id)
