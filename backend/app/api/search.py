from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.clip_service import clip_service

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
    result = clip_service.analyze_image(image_bytes)

    return {
        "status": "ok",
        "filename": image.filename,
        "category": result["category"],
        "confidence": result["confidence"],
        "all_scores": result["all_scores"]
    }