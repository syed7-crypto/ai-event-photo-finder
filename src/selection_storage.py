import os
import json
from src.candidate_selector import classify_photo
from src.face_detector import detect_faces

def save_selection(folder_name, folder_id, best_images):
    os.makedirs("selected", exist_ok=True)

    file_path = f"selected/{folder_id}.json"

    images = []

    for image in best_images:
        face_count= detect_faces(image)
        image = {
            "id": image["id"],
            "name": image["name"],
            "blur_score": image["blur_score"],
            "face_count": face_count,
            "photo_type": classify_photo(face_count)
        }

        images.append(image)

    data = {
        "folder_name": folder_name,
        "folder_id": folder_id,
        "selected_count": len(best_images),
        "images": images
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)