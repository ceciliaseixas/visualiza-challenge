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
### 🧪 Testes

Este projeto utiliza `pytest` para validar os endpoints da API. Os testes estão localizados no diretório `src/tests`.

#### ▶ Como rodar os testes:

1. Ative o ambiente virtual:
   ```bash
   .venv\Scripts\activate

### 💜 Agradecimento

Agradeço por dedicar seu tempo para conhecer este projeto.  
A Visualiza API foi desenvolvida como parte de um desafio técnico, buscando boas práticas e clareza.  

