from fastapi import APIRouter, UploadFile, File, HTTPException

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
    
    # respuesta de prueba
    return {
        "status": "ok",
        "filename": image.filename,
        "size_bytes": len(image_bytes),
        "message": "Imagen recibida correctamente"
    }