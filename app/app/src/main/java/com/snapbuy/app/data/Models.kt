package com.snapbuy.app.data

data class Product(
    val name: String,
    val price: Double,
    val rating: Double,
    val reviews: Int,
    val store: String,
    val url: String,
    val image_url: String,
    val score: Double,
    val badge: String?
)

data class SearchResponse(
    val search_id: String,
    val category: String,
    val confidence: Double,
    val total_results: Int,
    val results: List<Product>,
    val from_cache: Boolean
)