# 🚀 Visualiza API

API desenvolvida para o desafio **Visualiza**, utilizando **FastAPI** e **Docker**.

---

## ✨ Sobre

Essa API foi construída com FastAPI e está dockerizada para facilitar o deploy e a execução em qualquer ambiente.  
Ao acessar o endpoint raiz `/`, a API retorna uma mensagem de boas-vindas personalizada, com informações sobre a aplicação.

---

## 🛠 Tecnologias

- Python 3.8+
- FastAPI
- Uvicorn
- Docker

---

## ▶ Como rodar o projeto

### 🔧 Pré-requisitos:
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/) instalado e rodando

### 🐳 Usando Docker:

```bash
# Clone o repositório
git clone https://github.com/ceciliaseixas/visualiza-challenge.git
cd visualiza-challenge

# Build da imagem e execução do container
docker-compose up --build

```
### 📄 Variáveis de Ambiente

Para que a API funcione corretamente, é necessário criar um arquivo `.env` na raiz do projeto com a seguinte variável:

```env
NASA_API_KEY=voOtNzFfIwodIC9Oh32AvNigD43CbaQCPXm7H8cq

```
## 🧪 Como rodar os testes:

1. Clone este repositório:
```bash
git clone https://github.com/cecilia­seixas/visualiza-challenge.git
cd visualiza-challenge

Os testes automatizados verificam se os principais endpoints estão funcionando corretamente e se a API responde como esperado.

Para executar os testes unitários da aplicação, utilize o comando abaixo a partir da raiz do projeto: 
        pytest tests --import-mode=importlib

```
### 💜 Agradecimento

Agradeço por dedicar seu tempo para conhecer este projeto.  
A Visualiza API foi desenvolvida como parte de um desafio técnico, buscando boas práticas e clareza.  

