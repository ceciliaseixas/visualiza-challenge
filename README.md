# 🚀 Visualiza API

API desenvolvida para o desafio **Visualiza**, utilizando **FastAPI**, **Docker** e **Pytest**.

---

## ✨ Sobre

Essa API foi construída com FastAPI e está dockerizada para facilitar o deploy e a execução em qualquer ambiente.  
Ao acessar o endpoint raiz `/`, a API retorna uma mensagem de boas‑vindas personalizada, com informações sobre a aplicação.

---

## 🛠 Tecnologias

- Python 3.11+  
- FastAPI  
- Uvicorn  
- Docker & Docker Compose  
- Pytest  

---

## ▶ Como rodar o projeto

### 🔧 Pré‑requisitos  
- [Python 3.11+](https://www.python.org/downloads/) *(para desenvolvimento local)*  
- [Docker](https://www.docker.com/) instalado e rodando  

### 🐳 Usando Docker Compose

```bash
# 1. Clone o repositório
git clone https://github.com/ceciliaseixas/visualiza-challenge.git
cd visualiza-challenge

# 2. Crie o arquivo .env e defina sua chave da NASA
echo "NASA_API_KEY=voOtNzFfIwodIC9Oh32AvNigD43CbaQCPXm7H8cq" > .env

# 3. Build e sobe o container em background
docker-compose up --build -d

# 4. Acesse a documentação Swagger no navegador
# http://localhost:8000/docs

````
### 📄 Variáveis de Ambiente

Para que a API funcione corretamente, é necessário criar um arquivo `.env` na raiz do projeto com a seguinte variável:

```env
NASA_API_KEY=[sua_chave_da_api]

```
### 🧪 Testes

Este projeto utiliza `pytest` para validar os endpoints da API. Os testes estão localizados no diretório `src/tests`.

#### ▶ Como rodar os testes:

### Local (fora do container)

#### Opcional: crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

#### Instale dependências
pip install -r requirements.txt

#### Execute os testes
pytest tests --import-mode=importlib

### Dentro do container Docker
docker-compose exec api pytest tests --import-mode=importlib

## 📦 Endpoints Disponíveis

| Método | Rota      | Descrição                                         |
|--------|-----------|---------------------------------------------------|
| GET    | `/`       | Mensagem de boas‑vindas e metadados da API        |
| GET    | `/health` | Verificação de status (`{"status":"ok"}`)         |
| GET    | `/apod`   | Metadados da “Imagem Astronômica do Dia” da NASA  |

### 💜 Agradecimento

Agradeço por dedicar seu tempo para conhecer este projeto.
A Visualiza API foi desenvolvida como parte de um desafio técnico, buscando boas práticas, clareza e confiabilidade. 

