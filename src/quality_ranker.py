from src.duplicate_detector import average_hash
from src.blur_detector import detect_blur

def analyze_image(image, image_info):

    analysis = {
        "id": image_info["id"],
        "name": image_info["name"],
        "blur_score": detect_blur(image),
        "hash": average_hash(image).tolist()
    }

    return analysis
