from app.repository.repo_list_car import repo_list_car


def service_list_car(limit: int, next_car: str | None):
    last_key = {"car_id": next_car} if next_car else None
    return repo_list_car(limit=limit, last_key=last_key)
