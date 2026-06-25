import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, project_root)

from app.backend.rag.image_loader import ImageLoader

loader = ImageLoader()

documents = loader.load_image(
    "data/images/sample.png"
)

print("=" * 50)

print(documents[0].page_content)