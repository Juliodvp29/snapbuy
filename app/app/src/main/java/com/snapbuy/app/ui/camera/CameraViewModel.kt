package com.snapbuy.app.ui.camera

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.snapbuy.app.data.SearchResponse
import com.snapbuy.app.network.RetrofitClient
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.toRequestBody

// Estados posibles de la pantalla
sealed class SearchState {
    object Idle : SearchState()
    object Loading : SearchState()
    data class Success(val response: SearchResponse) : SearchState()
    data class Error(val message: String) : SearchState()
}

class CameraViewModel : ViewModel() {

    private val _searchState = MutableStateFlow<SearchState>(SearchState.Idle)
    val searchState: StateFlow<SearchState> = _searchState

    fun searchByImage(imageBytes: ByteArray) {
        viewModelScope.launch {
            _searchState.value = SearchState.Loading

            try {
                val requestBody = imageBytes.toRequestBody("image/jpeg".toMediaTypeOrNull())
                val imagePart = MultipartBody.Part.createFormData("image", "photo.jpg", requestBody)

                val response = RetrofitClient.apiService.searchByImage(imagePart)
                _searchState.value = SearchState.Success(response)

            } catch (e: Exception) {
                _searchState.value = SearchState.Error(e.message ?: "Error desconocido")
            }
        }
    }

    fun resetState() {
        _searchState.value = SearchState.Idle
    }
}