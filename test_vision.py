from app.multimodal.vision_analyzer import VisionAnalyzer

vision = VisionAnalyzer()

result = vision.analyze(
    "uploads/Screenshot 2026-06-24 231046.png"
)

print(result)