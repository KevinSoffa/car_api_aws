# 📡 API Cars - Python | FastAPI | AWS | DynamoDB
<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>

Esta aplicação é uma **API REST desenvolvida em FastAPI**, com foco em **operações de atualização no DynamoDB da AWS**, utilizando **Boto3** como SDK oficial para comunicação com os serviços AWS.

O projeto segue boas práticas de **arquitetura em camadas**, garantindo organização, escalabilidade, facilidade de testes e manutenção do código.

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

## 🔁 Separação de Responsabilidades

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

---

## 🎯 Objetivo da API
- Criar registros no DynamoDb de forma segura e performática
- Atualizar registros no DynamoDB de forma segura e performática
- Abstrair a complexidade do Boto3 através de uma API REST
- Servir como base para integrações com sistemas externos
- Aplicar boas práticas de backend e cloud AWS

---