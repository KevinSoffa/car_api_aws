from app.repository.repo_get_car import repo_get_car


def service_get_car(car_id: str):
    return repo_get_car(car_id)
