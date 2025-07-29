# 🚀 Visualiza API

[![CI](https://github.com/ceciliaseixas/visualiza-challenge/actions/workflows/main.yml/badge.svg)](https://github.com/ceciliaseixas/visualiza-challenge/actions/workflows/main.yml)

API desenvolvida em **FastAPI**, empacotada com **Docker** e validada com **pytest**.

---

## 📚 Sobre

Integração com a [API APOD da NASA](https://api.nasa.gov/) para exibir os metadados da “Imagem Astronômica do Dia”.

---

## ⚙️ Endpoints Disponíveis

| Método | Rota      | Descrição                                         |
|:------:|:---------:|:--------------------------------------------------|
| GET    | `/`       | Mensagem de boas‑vindas e metadados da API        |
| GET    | `/health` | Verificação de status (`{"status":"ok"}`)         |
| GET    | `/apod`   | Metadados da “Imagem Astronômica do Dia” da NASA  |

## 📡 Endpoint `/apod`

Retorna os metadados da “Imagem Astronômica do Dia” fornecida pela NASA, incluindo título, explicação, data, autor, tipo de mídia e URLs da imagem (comum e em HD).

```
GET /apod

```
### 🔁 Exemplo de Resposta

```json
{
  "copyright": "George Chatzifrantzis",
  "date": "2025-07-29",
  "explanation": "Is the Helix Nebula looking at you? No, not in any biological sense, but it does look quite like an eye...",
  "hdurl": "https://apod.nasa.gov/apod/image/2507/Helix_GC_2332.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "A Helix Nebula Deep Field",
  "url": "https://apod.nasa.gov/apod/image/2507/Helix_GC_1080.jpg"
}
```

### ⚠️ Possíveis Erros

- `503`: Erro ao tentar se comunicar com a API da NASA

---

## 🛠 Tecnologias

- Python 3.8+  
- FastAPI  
- Uvicorn  
- Docker & Docker Compose  
- pytest  

---

## ⚙️ Como rodar

### Pré‑requisitos

- [Python 3.8+](https://www.python.org/downloads/)  
- [Docker](https://www.docker.com/)  

### 1) Local (sem Docker)

```bash
git clone https://github.com/ceciliaseixas/visualiza-challenge.git
cd visualiza-challenge

# (opcional) criar e ativar venv
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

pip install -r requirements.txt

# criar .env na raiz do projeto
echo "NASA_API_KEY=SUA_CHAVE_AQUI" > .env

# iniciar API
uvicorn src.main:app --reload

```

#### Abra no navegador:
http://localhost:8000
http://localhost:8000/docs

#### Com Docker Compose
docker-compose up --build
A API ficará disponível em http://localhost:8000.


### 📄 Variáveis de Ambiente

Para que a API funcione corretamente, é necessário criar um arquivo `.env` na raiz do projeto com a seguinte variável:

```env
NASA_API_KEY=[sua_chave_da_api]

```
### 🧪 Testes

Este projeto utiliza `pytest` para validar os endpoints da API. Os testes estão localizados no diretório `tests/`.

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

#### No CI (GitHub Actions)
O workflow acionado em cada push na `main`:
1. Roda `pytest tests --import-mode=importlib`
2. Se passar, builda e faz push da imagem Docker (tags `latest` e `SHA`)

### 💜 Agradecimento

Agradeço por dedicar seu tempo para conhecer este projeto.
A Visualiza API foi desenvolvida como parte de um desafio técnico, buscando boas práticas, clareza e confiabilidade. 


