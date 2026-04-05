from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Inicializa o aplicativo FastAPI
app = FastAPI(
    title="Flash-Dash API",
    description="Motor de Business Intelligence para PMEs",
    version="0.1.0"
)

# Configuração de CORS (Permite que o Flutter converse com o Python)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "⚡ Bem-vindo ao Motor de BI do Flash-Dash!",
        "status": "online",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/v1/health")
def health_check():
    """
    Endpoint para o QA (Pedro) verificar a saúde do sistema.
    """
    return {
        "status": "ok",
        "database": "disconnected"
    }