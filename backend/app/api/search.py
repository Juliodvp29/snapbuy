from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.clip_service import clip_service
from app.services.mock_store import search_mock
from app.services.ranking import rank_products
import uuid

router = APIRouter()

@router.post("/search")
async def search_by_image(image: UploadFile = File(...)):

    # Validar que sea una imagen
    if not image.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="El archivo debe ser una imagen"
        )

    # Leer la imagen
    image_bytes = await image.read()

    # Analizar con CLIP
    clip_result = clip_service.analyze_image(image_bytes)
    category = clip_result["category"]
    confidence = clip_result["confidence"]

    # Buscar productos (mock)
    products = search_mock(category)

    # Aplicar ranking
    ranked_products = rank_products(products)

    return {
        "search_id": str(uuid.uuid4()),
        "category": category,
        "confidence": confidence,
        "total_results": len(ranked_products),
        "results": ranked_products
    }