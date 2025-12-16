from app.service.service_create_car import service_create_car
from app.service.service_delete_car import service_delete_car
from app.service.service_update_car import service_update_car
from app.service.service_list_car import service_list_car
from app.models.car_dto_updated import CarUpdateDTO
from app.models.car_dto import CarDTO
from fastapi import HTTPException
import pytest


##############################################
### TESTE DE CRIAÇÃO
##############################################
def test_service_create_car_success(mocker):
    # Arrange
    dto = CarDTO(
        nome="Civic",
        marca="Honda",
        modelo="EX",
        ano=2022,
        valor=90000
    )

    mock_repo = mocker.patch(
        "app.service.service_create_car.repo_create_car",
        return_value={"message": "Carro criado com sucesso"}
    )

    # Act
    response = service_create_car(dto)

    # Assert
    assert response == {"message": "Carro criado com sucesso"}
    mock_repo.assert_called_once()

    dao_passado = mock_repo.call_args[0][0]
    assert dao_passado.nome == "Civic"
    assert dao_passado.valor == 90000

##############################################
### TESTE DE APAGAR
##############################################
def test_service_delete_car_success(mocker):
    # Arrange
    car_id = "123-abc"

    mock_repo = mocker.patch(
        "app.service.service_delete_car.repo_delete_car",
        return_value={"message": "Carro deletado com sucesso"}
    )

    # Act
    response = service_delete_car(car_id)

    # Assert
    assert response == {"message": "Carro deletado com sucesso"}
    mock_repo.assert_called_once_with(car_id)

#################################################
### TESTE ATUALIZAÇÃO
#################################################
def test_service_update_car_success(mocker):
    # Arrange
    car_id = "123"
    dto = CarUpdateDTO(
        modelo="GT Turbo",
        valor=150000
    )

    mock_repo = mocker.patch(
        "app.service.service_update_car.repo_update_car",
        return_value={
            "car_id": car_id,
            "modelo": "GT Turbo",
            "valor": 150000
        }
    )

    # Act
    response = service_update_car(car_id, dto)

    # Assert
    assert response["car_id"] == car_id
    assert response["modelo"] == "GT Turbo"
    assert response["valor"] == 150000

    mock_repo.assert_called_once_with(
        car_id,
        {
            "modelo": "GT Turbo",
            "valor": 150000
        }
    )

def test_service_update_car_no_fields_error():
    car_id = "123"
    dto = CarUpdateDTO()  # tudo None

    with pytest.raises(HTTPException) as exc:
        service_update_car(car_id, dto)

    assert exc.value.status_code == 400
    assert exc.value.detail == "Nenhum campo informado para atualização"

#################################################
### LISTAGEM FULL
#################################################
def test_service_list_car_without_next_key(mocker):
    # Arrange
    limit = 10

    mock_repo = mocker.patch(
        "app.service.service_list_car.repo_list_car",
        return_value={
            "items": [
                {"car_id": "1", "nome": "Civic"},
                {"car_id": "2", "nome": "Corolla"}
            ],
            "next_car": None
        }
    )

    # Act
    response = service_list_car(limit=limit, next_car=None)

    # Assert
    assert len(response["items"]) == 2
    assert response["next_car"] is None

    mock_repo.assert_called_once_with(
        limit=limit,
        last_key=None
    )

def test_service_list_car_with_next_key(mocker):
    # Arrange
    limit = 5
    next_car = "abc-123"

    mock_repo = mocker.patch(
        "app.service.service_list_car.repo_list_car",
        return_value={
            "items": [
                {"car_id": "3", "nome": "Porsche"},
                {"car_id": "4", "nome": "BMW"}
            ],
            "next_car": "xyz-999"
        }
    )

    # Act
    response = service_list_car(limit=limit, next_car=next_car)

    # Assert
    assert response["next_car"] == "xyz-999"
    assert response["items"][0]["nome"] == "Porsche"

    mock_repo.assert_called_once_with(
        limit=limit,
        last_key={"car_id": next_car}
    )
