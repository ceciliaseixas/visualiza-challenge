# Etapa 1: Imagem base com Python
FROM python:3.10-slim

# Cria diretório da aplicação
WORKDIR /app

# Copia arquivos para dentro do container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta que o FastAPI vai rodar
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
