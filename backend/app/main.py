from fastapi import FastAPI
from dotenv import load_dotenv
from app.api import search

load_dotenv()

app = FastAPI(
    title="SnapBuy API",
    description="Backend para búsqueda visual de productos",
    version="0.1.0"
)

# Rutas
app.include_router(search.router, prefix="/api/v1", tags=["search"])

@app.get("/")
def root():
    return {"status": "ok", "message": "SnapBuy API corriendo"}

@app.get("/health")
def health():
    return {"status": "healthy"}