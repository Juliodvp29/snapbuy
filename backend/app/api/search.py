from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.clip_service import clip_service
from app.services.mock_store import search_mock
from app.services.ranking import rank_products
from app.database import get_db
from app.models.models import Product, ProductPrice, Search, SearchResult
import uuid
import hashlib

router = APIRouter()

@router.post("/search")
async def search_by_image(image: UploadFile = File(...), db: Session = Depends(get_db)):

    # Validar que sea una imagen
    if not image.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="El archivo debe ser una imagen"
        )

    # Leer la imagen
    image_bytes = await image.read()

    # Generar hash de la imagen (para caché futura)
    image_hash = hashlib.md5(image_bytes).hexdigest()

    # Analizar con CLIP
    clip_result = clip_service.analyze_image(image_bytes)
    category = clip_result["category"]
    confidence = clip_result["confidence"]

    # Buscar productos (mock)
    products = search_mock(category)

    # Aplicar ranking
    ranked_products = rank_products(products)

    # Guardar búsqueda en PostgreSQL
    search = Search(
        image_hash=image_hash,
        category=category,
        confidence=confidence
    )
    db.add(search)

    # Guardar productos y resultados
    for rank, product_data in enumerate(ranked_products, start=1):
        
        # Buscar si el producto ya existe por URL
        product = db.query(Product).filter(
            Product.product_url == product_data["url"]
        ).first()

        # Si no existe, crearlo
        if not product:
            product = Product(
                name=product_data["name"],
                category=category,
                image_url=product_data["image_url"],
                store=product_data["store"],
                product_url=product_data["url"]
            )
            db.add(product)
            db.flush()

            # Guardar precio
            price = ProductPrice(
                product_id=product.id,
                price=product_data["price"],
                currency="USD"
            )
            db.add(price)

        # Guardar resultado de búsqueda
        search_result = SearchResult(
            search_id=search.id,
            product_id=product.id,
            score=product_data["score"],
            rank=rank,
            badge=product_data.get("badge")
        )
        db.add(search_result)

    db.commit()

    return {
        "search_id": str(search.id),
        "category": category,
        "confidence": confidence,
        "total_results": len(ranked_products),
        "results": ranked_products
    }