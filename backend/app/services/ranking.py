def calculate_score(product: dict, price_min: float, price_max: float, reviews_max: int) -> float:
    
    # Normalizar rating (0 a 1)
    rating_norm = product["rating"] / 5.0

    # Normalizar precio (más barato = mejor score)
    if price_max == price_min:
        price_score = 1.0
    else:
        price_score = 1 - ((product["price"] - price_min) / (price_max - price_min))

    # Normalizar reviews con escala logarítmica
    import math
    if reviews_max == 0:
        review_norm = 0.0
    else:
        review_norm = math.log(1 + product["reviews"]) / math.log(1 + reviews_max)

    w1 = 0.45  # rating
    w2 = 0.35  # precio
    w3 = 0.20  # reviews

    score = (w1 * rating_norm) + (w2 * price_score) + (w3 * review_norm)
    return round(score, 4)


def assign_badge(product: dict, all_products: list) -> str:
    prices = [p["price"] for p in all_products]
    ratings = [p["rating"] for p in all_products]

    if product["price"] == min(prices):
        return "cheapest"
    if product["rating"] == max(ratings) and product["reviews"] >= 50:
        return "top_rated"
    if product["reviews"] == max(p["reviews"] for p in all_products):
        return "most_reviewed"
    return None


def rank_products(products: list) -> list:
    if not products:
        return []

    price_min = min(p["price"] for p in products)
    price_max = max(p["price"] for p in products)
    reviews_max = max(p["reviews"] for p in products)

    # Calcular score a cada producto
    for product in products:
        product["score"] = calculate_score(product, price_min, price_max, reviews_max)

    # Ordenar por score descendente
    products.sort(key=lambda x: x["score"], reverse=True)

    # Asignar badges
    for product in products:
        product["badge"] = assign_badge(product, products)

    # Al primero siempre le ponemos best_value
    if products:
        products[0]["badge"] = "best_value"

    return products