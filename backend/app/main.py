from fastapi import FastAPI
from dotenv import load_dotenv

# Carga las variables de entorno desde .env
load_dotenv()

app = FastAPI(
    title="SnapBuy API",
    description="Backend para búsqueda visual de productos",
    version="0.1.0"    
)

@app.get("/")
def root():
    return {"status": "ok", "message": "SnapBuy API corriendo"}

@app.get("/health")
def health():
    return {"status": "healthy"}