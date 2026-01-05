from fastapi import APIRouter, HTTPException, status, Depends
from ..service.service_auth import service_authenticate_user
from app.security.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
#from decouple import config


router_auth = APIRouter(tags=["Auth"])


@router_auth.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Passa email e senha vindos da camada Service
    user = service_authenticate_user(
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválidos"
        )

    token = create_access_token(
        {"sub": user["email"]}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }