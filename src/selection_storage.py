import os
import json


def save_selection(folder_name, folder_id, best_images):

    os.makedirs("selected", exist_ok=True)

    file_path = f"selected/{folder_id}.json"

    images = []

    for image in best_images:

        selected_image = {
            "id": image["id"],
            "name": image["name"],
            "blur_score": image["blur_score"]
        }

        images.append(selected_image)

    data = {
        "folder_name": folder_name,
        "folder_id": folder_id,
        "selected_count": len(best_images),
        "images": images
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)