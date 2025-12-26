from app.service.service_update_car import service_update_car
from app.security.dependencies import get_current_user
from app.models.car_dto_updated import CarUpdateDTO
from fastapi import APIRouter, Depends


router_update_car = APIRouter(tags=["Cars"])

@router_update_car.patch(
    "/v1/cars/{car_id}",
    summary="Atualizar carro por ID",
    description="Atualiza parcialmente um carro no DynamoDB [ AWS ]."
)
def update_car(
    car_id: str, 
    dto: CarUpdateDTO,
    user=Depends(get_current_user)
):
    return service_update_car(car_id, dto)
