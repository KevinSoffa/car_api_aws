from app.repository.repo_delete_car import repo_delete_car


def service_delete_car(car_id: str):
    return repo_delete_car(car_id)
