import os
import json
import numpy as np

def save_analysis(folder_name, folder_id, results):

    os.makedirs("analysis", exist_ok=True)

    file_path = f"analysis/{folder_id}.json"

    images_to_save = []

    for image in results:
        image_copy = image.copy()
        image_copy["hash"] = image_copy["hash"].tolist()
        images_to_save.append(image_copy)

    data = {
    "folder_name": folder_name,
    "folder_id": folder_id,
    "images": images_to_save
    }   

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_analysis(folder_id):

    file_path = f"analysis/{folder_id}.json"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:
        data = json.load(file)

    for image in data["images"]:
        image["hash"] = np.array(image["hash"])

    return data
    