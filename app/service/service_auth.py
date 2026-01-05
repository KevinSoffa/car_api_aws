from ..repository.repo_user import get_user_by_email
from ..security.password import verify_password


def service_authenticate_user(email: str, password: str):
    # Busca o usuário na tabela Users do DynamoDB usando o email (Camada Repository)
    user = get_user_by_email(email)

    # Se não encontrou nenhum registro, o usuário não existe (retorna None)
    if not user:
        return None

    # Verifica se a senha informada bate com o hash salvo no DynamoDB
    # (bcrypt + passlib fazem essa validação com segurança)
    if not verify_password(password, user["password"]):
        return None

    # Se o usuário existe e a senha está correta, retorna o usuário completo
    # Esse objeto será usado para gerar o JWT e identificar o usuário logado
    return user

