from fastapi.openapi.utils import get_openapi
from app.controller.router import router
from fastapi import FastAPI


app = FastAPI(
    title="Cars API",
    description="""
API para gerenciamento de carros usando **FastAPI**, **DynamoDB** e arquitetura limpa.

## 🔧 Recursos disponíveis:
- Criar carro
- Buscar carro por ID
- Listar todos os carros
- Atualizar carro
- Deletar carro

A API segue arquitetura em camadas:


## 📦 Tecnologias:
- FastAPI
- Python
- DynamoDB
- Boto3
""",
    version="1.0.0",
    contact={
        "name": "Kevin Soffa",
        "email": "kevin@example.com",
        "url": "https://github.com/seu-github",
    }
)

app.include_router(router)


# 🔹 Geração personalizada do OpenAPI (Swagger)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Cars API - FastApi / AWS",
        version="1.0.0",
        description="Documentação OpenAPI Cars API.",
        routes=app.routes,
    )

    # Logo opcional
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cdn-icons-png.flaticon.com/512/743/743007.png"
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
