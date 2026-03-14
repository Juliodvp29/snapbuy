import random

MOCK_PRODUCTS = {
    "headphones": [
        {"name": "Sony WH-1000XM5", "price": 299.99, "rating": 4.8, "reviews": 4521, "store": "Amazon", "url": "https://amazon.com/producto/1", "image_url": "https://picsum.photos/200?random=1"},
        {"name": "JBL Tune 520BT", "price": 49.99, "rating": 4.3, "reviews": 1832, "store": "eBay", "url": "https://ebay.com/producto/2", "image_url": "https://picsum.photos/200?random=2"},
        {"name": "Anker Soundcore Q20", "price": 35.99, "rating": 4.5, "reviews": 9823, "store": "AliExpress", "url": "https://aliexpress.com/producto/3", "image_url": "https://picsum.photos/200?random=3"},
        {"name": "Bose QuietComfort 45", "price": 249.99, "rating": 4.7, "reviews": 3201, "store": "Amazon", "url": "https://amazon.com/producto/4", "image_url": "https://picsum.photos/200?random=4"},
        {"name": "Xiaomi Redmi Buds 4", "price": 24.99, "rating": 4.1, "reviews": 2145, "store": "AliExpress", "url": "https://aliexpress.com/producto/5", "image_url": "https://picsum.photos/200?random=5"},
        {"name": "Sennheiser HD 450BT", "price": 99.99, "rating": 4.4, "reviews": 1200, "store": "eBay", "url": "https://ebay.com/producto/6", "image_url": "https://picsum.photos/200?random=6"},
        {"name": "Edifier W820NB", "price": 59.99, "rating": 4.3, "reviews": 870, "store": "AliExpress", "url": "https://aliexpress.com/producto/7", "image_url": "https://picsum.photos/200?random=7"},
    ],
    "a phone case": [
        {"name": "Spigen Ultra Hybrid", "price": 12.99, "rating": 4.6, "reviews": 8734, "store": "Amazon", "url": "https://amazon.com/producto/8", "image_url": "https://picsum.photos/200?random=8"},
        {"name": "OtterBox Defender", "price": 39.99, "rating": 4.7, "reviews": 5612, "store": "Amazon", "url": "https://amazon.com/producto/9", "image_url": "https://picsum.photos/200?random=9"},
        {"name": "Caseology Parallax", "price": 14.99, "rating": 4.4, "reviews": 3201, "store": "eBay", "url": "https://ebay.com/producto/10", "image_url": "https://picsum.photos/200?random=10"},
        {"name": "Ringke Fusion", "price": 9.99, "rating": 4.3, "reviews": 4102, "store": "AliExpress", "url": "https://aliexpress.com/producto/11", "image_url": "https://picsum.photos/200?random=11"},
        {"name": "ESR Air Armor", "price": 8.99, "rating": 4.2, "reviews": 2987, "store": "AliExpress", "url": "https://aliexpress.com/producto/12", "image_url": "https://picsum.photos/200?random=12"},
        {"name": "Totallee Thin Case", "price": 29.99, "rating": 4.5, "reviews": 1543, "store": "eBay", "url": "https://ebay.com/producto/13", "image_url": "https://picsum.photos/200?random=13"},
    ],
    "a smartphone": [
        {"name": "Samsung Galaxy A55", "price": 349.99, "rating": 4.5, "reviews": 6123, "store": "Amazon", "url": "https://amazon.com/producto/14", "image_url": "https://picsum.photos/200?random=14"},
        {"name": "Xiaomi Redmi Note 13", "price": 199.99, "rating": 4.4, "reviews": 8921, "store": "AliExpress", "url": "https://aliexpress.com/producto/15", "image_url": "https://picsum.photos/200?random=15"},
        {"name": "Motorola Moto G84", "price": 229.99, "rating": 4.3, "reviews": 3412, "store": "eBay", "url": "https://ebay.com/producto/16", "image_url": "https://picsum.photos/200?random=16"},
        {"name": "Google Pixel 7a", "price": 449.99, "rating": 4.6, "reviews": 4231, "store": "Amazon", "url": "https://amazon.com/producto/17", "image_url": "https://picsum.photos/200?random=17"},
        {"name": "OnePlus Nord CE 3", "price": 279.99, "rating": 4.4, "reviews": 2987, "store": "AliExpress", "url": "https://aliexpress.com/producto/18", "image_url": "https://picsum.photos/200?random=18"},
    ],
    "a laptop": [
        {"name": "Acer Aspire 5", "price": 549.99, "rating": 4.4, "reviews": 5231, "store": "Amazon", "url": "https://amazon.com/producto/19", "image_url": "https://picsum.photos/200?random=19"},
        {"name": "Lenovo IdeaPad 3", "price": 499.99, "rating": 4.3, "reviews": 4102, "store": "eBay", "url": "https://ebay.com/producto/20", "image_url": "https://picsum.photos/200?random=20"},
        {"name": "HP Pavilion 15", "price": 629.99, "rating": 4.5, "reviews": 3871, "store": "Amazon", "url": "https://amazon.com/producto/21", "image_url": "https://picsum.photos/200?random=21"},
        {"name": "Xiaomi RedmiBook 15", "price": 399.99, "rating": 4.2, "reviews": 1987, "store": "AliExpress", "url": "https://aliexpress.com/producto/22", "image_url": "https://picsum.photos/200?random=22"},
    ],
    "a keyboard": [
        {"name": "Logitech K380", "price": 39.99, "rating": 4.5, "reviews": 12453, "store": "Amazon", "url": "https://amazon.com/producto/23", "image_url": "https://picsum.photos/200?random=23"},
        {"name": "Keychron K2", "price": 89.99, "rating": 4.7, "reviews": 8921, "store": "Amazon", "url": "https://amazon.com/producto/24", "image_url": "https://picsum.photos/200?random=24"},
        {"name": "Royal Kludge RK61", "price": 34.99, "rating": 4.3, "reviews": 5432, "store": "AliExpress", "url": "https://aliexpress.com/producto/25", "image_url": "https://picsum.photos/200?random=25"},
        {"name": "Razer BlackWidow V3", "price": 129.99, "rating": 4.6, "reviews": 6234, "store": "eBay", "url": "https://ebay.com/producto/26", "image_url": "https://picsum.photos/200?random=26"},
    ],
    "a mouse": [
        {"name": "Logitech MX Master 3", "price": 99.99, "rating": 4.8, "reviews": 15234, "store": "Amazon", "url": "https://amazon.com/producto/27", "image_url": "https://picsum.photos/200?random=27"},
        {"name": "Razer DeathAdder V3", "price": 69.99, "rating": 4.6, "reviews": 8123, "store": "eBay", "url": "https://ebay.com/producto/28", "image_url": "https://picsum.photos/200?random=28"},
        {"name": "Xiaomi Mi Mouse", "price": 14.99, "rating": 4.1, "reviews": 3421, "store": "AliExpress", "url": "https://aliexpress.com/producto/29", "image_url": "https://picsum.photos/200?random=29"},
        {"name": "HP X1000", "price": 19.99, "rating": 4.0, "reviews": 2134, "store": "Amazon", "url": "https://amazon.com/producto/30", "image_url": "https://picsum.photos/200?random=30"},
    ],
    "a backpack": [
        {"name": "Samsonite Guardit 2.0", "price": 79.99, "rating": 4.5, "reviews": 4231, "store": "Amazon", "url": "https://amazon.com/producto/31", "image_url": "https://picsum.photos/200?random=31"},
        {"name": "Xiaomi Mi Backpack", "price": 29.99, "rating": 4.3, "reviews": 6543, "store": "AliExpress", "url": "https://aliexpress.com/producto/32", "image_url": "https://picsum.photos/200?random=32"},
        {"name": "Targus CityLite", "price": 49.99, "rating": 4.4, "reviews": 2987, "store": "eBay", "url": "https://ebay.com/producto/33", "image_url": "https://picsum.photos/200?random=33"},
    ],
    "a watch": [
        {"name": "Casio F-91W", "price": 19.99, "rating": 4.7, "reviews": 23451, "store": "Amazon", "url": "https://amazon.com/producto/34", "image_url": "https://picsum.photos/200?random=34"},
        {"name": "Xiaomi Mi Band 8", "price": 34.99, "rating": 4.4, "reviews": 12341, "store": "AliExpress", "url": "https://aliexpress.com/producto/35", "image_url": "https://picsum.photos/200?random=35"},
        {"name": "Fossil Gen 6", "price": 199.99, "rating": 4.3, "reviews": 3421, "store": "eBay", "url": "https://ebay.com/producto/36", "image_url": "https://picsum.photos/200?random=36"},
        {"name": "Samsung Galaxy Watch 6", "price": 249.99, "rating": 4.5, "reviews": 5432, "store": "Amazon", "url": "https://amazon.com/producto/37", "image_url": "https://picsum.photos/200?random=37"},
    ],
}

GENERIC_PRODUCTS = [
    {"name": "Producto genérico A", "price": 19.99, "rating": 4.0, "reviews": 500, "store": "Amazon", "url": "https://amazon.com/producto/99", "image_url": "https://picsum.photos/200?random=40"},
    {"name": "Producto genérico B", "price": 34.99, "rating": 3.8, "reviews": 320, "store": "eBay", "url": "https://ebay.com/producto/100", "image_url": "https://picsum.photos/200?random=41"},
    {"name": "Producto genérico C", "price": 49.99, "rating": 4.2, "reviews": 780, "store": "AliExpress", "url": "https://aliexpress.com/producto/101", "image_url": "https://picsum.photos/200?random=42"},
]

def search_mock(category: str) -> list:
    products = MOCK_PRODUCTS.get(category, GENERIC_PRODUCTS)
    result = []
    for p in products:
        product = p.copy()
        variation = random.uniform(-2, 2)
        product["price"] = round(product["price"] + variation, 2)
        result.append(product)
    return result