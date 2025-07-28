from fastapi import FastAPI
import os
import httpx
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env
NASA_API_KEY = os.getenv("NASA_API_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "success",
        "api": "Visualiza API",
        "version": "1.0.0",
        "author": "Ana Cecília Seixas",
        "message": "👋 Seja bem-vindo(a)! Esta é a API oficial do desafio Visualiza 🚀"
    }

@app.get("/health")
def check_health():
    return {"status": "ok"}

@app.get("/apod")
async def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return data
