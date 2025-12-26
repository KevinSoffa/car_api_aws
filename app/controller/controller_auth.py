from fastapi import APIRouter, HTTPException, status, Depends
from app.security.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from decouple import config


# MOCK Usuários [ Poderia vim de um banco ou usuário logado ]
user_auth = config('USER_AUTH')
password_auth = config('PASSWORD_AUTH')

router_auth = APIRouter(tags=["Auth"])

@router_auth.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Usuário fake (estudo) => MOCK
    if form_data.username != str(user_auth) or form_data.password != str(password_auth):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválidos"
        )

    token = create_access_token({"sub": form_data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
