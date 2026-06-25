from app.multimodal.multimodal_analyzer import MultimodalAnalyzer

analyzer = MultimodalAnalyzer()

result = analyzer.analyze(
"uploads/Screenshot 2026-06-24 231046.png"
)

print(result)
