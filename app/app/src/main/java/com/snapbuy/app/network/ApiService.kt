package com.snapbuy.app.network

import com.snapbuy.app.data.SearchResponse
import okhttp3.MultipartBody
import retrofit2.http.Multipart
import retrofit2.http.POST
import retrofit2.http.Part

interface ApiService {
    @Multipart
    @POST("api/v1/search")
    suspend fun searchByImage(
        @Part image: MultipartBody.Part
    ): SearchResponse
}