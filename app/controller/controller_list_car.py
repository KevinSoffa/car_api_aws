from app.service.service_list_car import service_list_car
from fastapi import APIRouter, Query
from typing import Optional


router_list_car = APIRouter(tags=["Cars"])

@router_list_car.get(
    "/v1/cars",
    summary="Listar carros",
    description="Lista carros com paginação."
)
def list_cars(
    limit: int = Query(10, ge=1, le=50),
    next_page: Optional[str] = Query(None) # Paginacao
):
    return service_list_car(limit=limit, next_car=next_page)
