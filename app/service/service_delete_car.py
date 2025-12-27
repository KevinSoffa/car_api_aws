from app.repository.repo_delete_car import repo_delete_car
from fastapi import HTTPException, status


def service_delete_car(car_id: str):
    car = repo_delete_car(car_id)

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ID não encontrado ou já Deletado"
        )
    return car

