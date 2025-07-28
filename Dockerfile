# Etapa de build
FROM python:3.11-slim AS builder

WORKDIR /app

# Instala dependências de sistema para compilar pacotes Python nativos
RUN apt-get update && apt-get install -y build-essential

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências no diretório /install
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt

# Etapa final da imagem
FROM python:3.11-slim

# Cria usuário para rodar a aplicação com menos privilégios
RUN useradd -m appuser
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

# Usa o usuário não-root
USER appuser

# Comando para iniciar o servidor com autoreload
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

