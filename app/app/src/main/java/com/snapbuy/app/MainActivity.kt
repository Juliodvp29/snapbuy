package com.snapbuy.app

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.runtime.*
import androidx.core.content.ContextCompat
import androidx.lifecycle.viewmodel.compose.viewModel
import com.snapbuy.app.ui.camera.CameraScreen
import com.snapbuy.app.ui.camera.CameraViewModel
import com.snapbuy.app.ui.results.ResultsScreen
import com.snapbuy.app.ui.theme.SnapBuyTheme

class MainActivity : ComponentActivity() {

    private val requestPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (!isGranted) finish()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Solicitar permiso de cámara si no lo tiene
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
            != PackageManager.PERMISSION_GRANTED) {
            requestPermissionLauncher.launch(Manifest.permission.CAMERA)
        }

        setContent {
            SnapBuyTheme {
                SnapBuyApp()
            }
        }
    }
}

@Composable
fun SnapBuyApp() {
    val viewModel: CameraViewModel = viewModel()
    var showResults by remember { mutableStateOf(false) }

    if (showResults) {
        ResultsScreen(
            onBack = { showResults = false },
            viewModel = viewModel
        )
    } else {
        CameraScreen(
            onResultsReady = { showResults = true },
            viewModel = viewModel
        )
    }
}