from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import io

# Categorías de productos a intentar identificar
PRODUCT_CATEGORIES = [
    "a phone case",
    "a laptop",
    "a smartphone",
    "headphones",
    "a keyboard",
    "a mouse",
    "a monitor",
    "a backpack",
    "shoes",
    "a watch",
    "a camera",
    "a tablet",
    "a book",
    "clothing",
    "a toy"
]

class CLIPService:
    def __init__(self):
        self.model = None
        self.processor = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load_model(self):
        print("Cargando modelo CLIP...")
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.model.to(self.device)
        print(f"Modelo CLIP cargado en {self.device}")

    def analyze_image(self, image_bytes: bytes) -> dict:
        if self.model is None:
            self.load_model()

        # Convertir bytes a imagen
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Procesar imagen y categorías
        inputs = self.processor(
            text=PRODUCT_CATEGORIES,
            images=image,
            return_tensors="pt",
            padding=True
        ).to(self.device)

        # Calcular similitud imagen vs categorías
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits_per_image
            probs = logits.softmax(dim=1)[0]

        # Encontrar la categoría con mayor probabilidad
        best_idx = probs.argmax().item()
        confidence = probs[best_idx].item()

        return {
            "category": PRODUCT_CATEGORIES[best_idx],
            "confidence": round(confidence, 4),
            "all_scores": {
                PRODUCT_CATEGORIES[i]: round(probs[i].item(), 4)
                for i in range(len(PRODUCT_CATEGORIES))
            }
        }

# Instancia global 
clip_service = CLIPService()