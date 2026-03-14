from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.clip_service import clip_service
from app.services.mock_store import search_mock
from app.services.ranking import rank_products
from app.services.cache_service import cache_service
from app.database import get_db
from app.models.models import Product, ProductPrice, Search, SearchResult
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

    # Generar hash de la imagen
    image_hash = hashlib.md5(image_bytes).hexdigest()

    # Verificar si hay resultado en caché
    cached = cache_service.get(image_hash)
    if cached:
        cached["from_cache"] = True
        return cached

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
    db.flush()  

    # Guardar productos y resultados
    for rank, product_data in enumerate(ranked_products, start=1):

        product = db.query(Product).filter(
            Product.product_url == product_data["url"]
        ).first()

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

            price = ProductPrice(
                product_id=product.id,
                price=product_data["price"],
                currency="USD"
            )
            db.add(price)

        search_result = SearchResult(
            search_id=search.id,
            product_id=product.id,
            score=product_data["score"],
            rank=rank,
            badge=product_data.get("badge")
        )
        db.add(search_result)

    db.commit()

    # Construir respuesta
    response = {
        "search_id": str(search.id),
        "category": category,
        "confidence": confidence,
        "total_results": len(ranked_products),
        "results": ranked_products,
        "from_cache": False
    }

    # Guardar en caché
    cache_service.set(image_hash, response)

    return response