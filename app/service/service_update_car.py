from app.repository.repo_update_car import repo_update_car
from app.models.car_dto_updated import CarUpdateDTO
from fastapi import HTTPException, status


def service_update_car(car_id: str, dto: CarUpdateDTO):
    dados_para_atualizar = dto.model_dump(exclude_none=True)

    if not dados_para_atualizar:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum campo informado para atualização"
        )

    # regra de negócio só se valor vier
    if "valor" in dados_para_atualizar and dados_para_atualizar["valor"] <= 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O valor do carro deve ser maior que 1000"
        )

    return repo_update_car(car_id, dados_para_atualizar)
