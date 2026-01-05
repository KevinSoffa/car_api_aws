# 📡 API Cars - Python | FastAPI | AWS | DynamoDB
<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>

Esta aplicação é uma **API REST desenvolvida em FastAPI**, com foco em **operações de atualização no DynamoDB da AWS**, utilizando **Boto3** como SDK oficial para comunicação com os serviços AWS.

O projeto segue boas práticas de **arquitetura em camadas**, garantindo organização, escalabilidade, facilidade de testes e manutenção do código.

---
## 📑 Índice

- [☁️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🧱 Arquitetura do Projeto](#-arquitetura-do-projeto)
- [🔁 Separação de Camadas](#-separação-de-camadas)
- [🎯 Objetivo da API](#-objetivo-da-api)
- [📘 Swagger](#swagger)
- [📌 Exemplo de Uso](#exemplo-de-uso)
  - [🔐 Login](#login--post---auth-)
  - [🟢 Criar Carro](#v1cars--post-)
  - [🔵 Listar Carros](#v1carslimitdefault_10next_pagetoken_next_page--get-)
  - [🔵 Buscar Carro por ID](#v1carscar_id--get-))
  - [🟣 Atualizar Carro](#v1carscar_id--patch-)
  - [🔴 Deletar Carro](#v1carscar_id--delete-)
- [☁️ DynamoDB (AWS)](#️dynamodb--aws-)
  - [🗄️Tabelas](#️tables)
    - [🗃️Table Cars](#️table-cars)
    - [🗃️Table Users](#️table-users)

---

## ☁️ Tecnologias Utilizadas
- Python 🐍
- FastAPI ⚡
- AWS DynamoDB ☁️
- Boto3 🔌
- Pydantic 📦
- Pytest 🧪

---

## 🧱 Arquitetura do Projeto

A aplicação segue o padrão de **arquitetura em camadas**, separando responsabilidades e evitando acoplamento entre regras de negócio, infraestrutura e exposição da API.
---

## 🔁 Separação de Camadas

### 🎮 Controller
Camada responsável por expor os **endpoints REST**, validar as requisições e retornar as respostas HTTP.  
Não contém regra de negócio nem acesso direto ao DynamoDB.

### ⚙️ Service
Centraliza as **regras de negócio** e validações.  
Coordena chamadas entre controllers e repositórios, garantindo consistência das operações.

### 🗄️ Repository
Responsável pela **integração com o DynamoDB**, utilizando **Boto3** para executar operações como:
- UpdateItem
- GetItem
- PutItem
- Query / Scan

Essa camada abstrai completamente a comunicação com a AWS.

### 📦 Models
Define os **DTOs**, schemas Pydantic e modelos utilizados para entrada e saída de dados da API.

### 🔐 Security
Gerencia autenticação e autorização, incluindo:
- JWT
- Validação de permissões
- Integração com mecanismos de segurança da AWS (quando aplicável)

### 🧪 Tests
Contém testes automatizados com **pytest**, garantindo confiabilidade das operações no DynamoDB (mockadas ou em ambiente de teste).
<div align="center">
  <img src="https://raw.githubusercontent.com/KevinSoffa/car_api_aws/refs/heads/master/img/test_01.png"/>
</div>
---

## 🎯 Objetivo da API
- Criar registros no DynamoDB de forma segura e performática
- Atualizar registros no DynamoDB de forma segura e performática
- Abstrair a complexidade do Boto3 através de uma API REST
- Servir como base para integrações com sistemas externos
- Aplicar boas práticas de backend e cloud AWS
---

## 📘Swagger
#### `/docs`
<div align="center">
  <img src="https://raw.githubusercontent.com/KevinSoffa/car_api_aws/refs/heads/master/img/swagger_01.png"/>
</div>

## 📌Exemplo de Uso

### 🔐`/login` **[ POST - Auth ]**
**form-urlencoded**
```
username:{email_user}
password:{password_user}
```
**Response**
Status Code `http 200` OK
```
{
	"access_token": "{token}",
	"token_type": "bearer"
}
```

**Response**
Status Code `http 401` Unauthorized
```
{
	"detail": "Usuário ou senha inválidos"
}
```
```
{
	"detail": "Token inválido ou expirado"
}
```
---


### 🟢`/v1/cars` **[ POST ]**
**Body**
```
{
  "nome": "string",
  "marca": "string",
  "modelo": "string",
  "ano": 0,
  "valor": 0
}
```
**Response**

Status Code `http 201` Criado com Sucesso
```
{
  "car_id": "97109191-7372-44e1-954f-db6132a9ee08",
  "nome": "Série 3",
  "marca": "BMW",
  "modelo": "320i M Sport",
  "ano": 2023,
  "valor": 320000
}
```
---
### 🔵`/v1/cars?limit={default_10}&next_page={token_next_page}` **[ GET ]**
**Response**

Status Code `http 200` OK
```
{
	"items": [
		{
			"ano": 2024,
			"marca": "Porsche",
			"valor": 1000000,
			"nome": "Carreira",
			"car_id": "1f80f12a-eca1-4d59-9011-09bce23854f6",
			"modelo": "GT Turbo"
		},
		{
			"ano": 2023,
			"marca": "Jeep",
			"valor": 210000,
			"nome": "Compass",
			"car_id": "43fb0a33-4dad-47b2-9b15-c81c426de731",
			"modelo": "Limited"
		}
	],
	"next_page": "43fb0a33-4dad-47b2-9b15-c81c426de731",
	"count": 2
}
```
---
### 🔵`/v1/cars/{car_id}` **[ GET ]**
**Response**
Status Code `http 200` OK
```
{
	"ano": 2023,
	"marca": "Tesla",
	"valor": 380000,
	"nome": "Model 3",
	"car_id": "763efdf7-feb2-4035-a68d-12c48601f69f",
	"modelo": "Long Range"
}
```
----
### 🟣`/v1/cars/{car_id}` **[ PATCH ]**
**Body**
```
{
  "nome": "string",
  "marca": "string",
  "modelo": "string",
  "ano": 0,
  "valor": 0
}
```
**Response**
Status Code `http 200` OK
```
{
  "ano": 2023,
  "marca": "Tesla",
  "valor": 380001,
  "nome": "Model 3",
  "car_id": "763efdf7-feb2-4035-a68d-12c48601f69f",
  "modelo": "Long Range"
}
```
---
### 🔴`/v1/cars/{car_id}` **[ DELETE ]**
Status Code `http 200` OK
**Response**
```
{
  "message": "Car deleted"
}
```
---
## ☁️DynamoDB [ AWS ]
### 🗄️Table's

<div align="center">
  <img src="https://raw.githubusercontent.com/KevinSoffa/car_api_aws/refs/heads/master/img/aws_tabelas.png"/>
</div>

### 🗃️Table `Cars`
#### 🐍Script Python para criação da tabela na AWS
```
import boto3


# ----------------------------
# CRIACAO DO DB NA AWS
#-----------------------------
dynamodb = boto3.client("dynamodb", region_name="us-east-1")
table_name = "Cars"

response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {"AttributeName": "car_id", "AttributeType": "S"},
    ],
    KeySchema=[
        {"AttributeName": "car_id", "KeyType": "HASH"},
    ],
    BillingMode="PAY_PER_REQUEST",
)

print("Tabela criada com sucesso:", response)
```
<div align="center">
  <img src="https://raw.githubusercontent.com/KevinSoffa/car_api_aws/refs/heads/master/img/aws_tabela_02.png"/>
</div>

---

### 🗃️Table `Users`
#### 🐍Script Python para criação da tabela na AWS
```
import boto3


# ----------------------------
# CRIAÇÃO DA TABELA USERS
# ----------------------------
dynamodb = boto3.client("dynamodb", region_name="us-east-1")

table_name = "Users"

response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {"AttributeName": "email", "AttributeType": "S"},
    ],
    KeySchema=[
        {"AttributeName": "email", "KeyType": "HASH"},
    ],
    BillingMode="PAY_PER_REQUEST",
)

print("Tabela criada com sucesso:", response)
```

<div align="center">
  <img src="https://raw.githubusercontent.com/KevinSoffa/car_api_aws/refs/heads/master/img/aws_tabela_users.png"/>
</div>