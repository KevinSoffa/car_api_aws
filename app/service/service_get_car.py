from app.repository.repo_get_car import repo_get_car
from fastapi import HTTPException, status


def service_get_car(car_id: str):
    car = repo_get_car(car_id)

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID não encontrado"
        )
    return car
