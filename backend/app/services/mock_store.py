import random

MOCK_PRODUCTS = {
    "headphones": [
        {"name": "Sony WH-1000XM5", "price": 299.99, "rating": 4.8, "reviews": 4521, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/1", "image_url": "https://picsum.photos/200?random=1"},
        {"name": "JBL Tune 520BT", "price": 49.99, "rating": 4.3, "reviews": 1832, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/2", "image_url": "https://picsum.photos/200?random=2"},
        {"name": "Anker Soundcore Q20", "price": 35.99, "rating": 4.5, "reviews": 9823, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/3", "image_url": "https://picsum.photos/200?random=3"},
        {"name": "Bose QuietComfort 45", "price": 249.99, "rating": 4.7, "reviews": 3201, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/4", "image_url": "https://picsum.photos/200?random=4"},
        {"name": "Xiaomi Redmi Buds 4", "price": 24.99, "rating": 4.1, "reviews": 2145, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/5", "image_url": "https://picsum.photos/200?random=5"},
    ],
    "a phone case": [
        {"name": "Spigen Ultra Hybrid", "price": 12.99, "rating": 4.6, "reviews": 8734, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/6", "image_url": "https://picsum.photos/200?random=6"},
        {"name": "OtterBox Defender", "price": 39.99, "rating": 4.7, "reviews": 5612, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/7", "image_url": "https://picsum.photos/200?random=7"},
        {"name": "Caseology Parallax", "price": 14.99, "rating": 4.4, "reviews": 3201, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/8", "image_url": "https://picsum.photos/200?random=8"},
        {"name": "Ringke Fusion", "price": 9.99, "rating": 4.3, "reviews": 4102, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/9", "image_url": "https://picsum.photos/200?random=9"},
        {"name": "ESR Air Armor", "price": 8.99, "rating": 4.2, "reviews": 2987, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/10", "image_url": "https://picsum.photos/200?random=10"},
    ],
    "a smartphone": [
        {"name": "Samsung Galaxy A55", "price": 349.99, "rating": 4.5, "reviews": 6123, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/11", "image_url": "https://picsum.photos/200?random=11"},
        {"name": "Xiaomi Redmi Note 13", "price": 199.99, "rating": 4.4, "reviews": 8921, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/12", "image_url": "https://picsum.photos/200?random=12"},
        {"name": "Motorola Moto G84", "price": 229.99, "rating": 4.3, "reviews": 3412, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/13", "image_url": "https://picsum.photos/200?random=13"},
    ],
}

GENERIC_PRODUCTS = [
    {"name": "Producto genérico A", "price": 19.99, "rating": 4.0, "reviews": 500, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/99", "image_url": "https://picsum.photos/200?random=20"},
    {"name": "Producto genérico B", "price": 34.99, "rating": 3.8, "reviews": 320, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/100", "image_url": "https://picsum.photos/200?random=21"},
    {"name": "Producto genérico C", "price": 49.99, "rating": 4.2, "reviews": 780, "store": "MercadoLibre", "url": "https://mercadolibre.com/producto/101", "image_url": "https://picsum.photos/200?random=22"},
]

def search_mock(category: str) -> list:
    products = MOCK_PRODUCTS.get(category, GENERIC_PRODUCTS)
    # Simula pequeñas variaciones de precio en cada llamada
    result = []
    for p in products:
        product = p.copy()
        variation = random.uniform(-2, 2)
        product["price"] = round(product["price"] + variation, 2)
        result.append(product)
    return result