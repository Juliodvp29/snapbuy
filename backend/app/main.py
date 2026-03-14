from fastapi import FastAPI
from dotenv import load_dotenv
from app.api import search
from app.database import engine, Base
from app.models import models

load_dotenv()

# Crear tablas en PostgreSQL
Base.metadata.create_all(bind=engine)

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