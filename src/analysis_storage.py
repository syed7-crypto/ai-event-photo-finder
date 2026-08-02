import os
import json

def save_analysis(folder_name, folder_id, results):

    os.makedirs("analysis", exist_ok=True)

    file_path = f"analysis/{folder_id}.json"

    data = {
        "folder_name": folder_name,
        "folder_id": folder_id,
        "images": results
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_analysis(folder_id):

    file_path = f"analysis/{folder_id}.json"

    if not os.path.exists(file_path):
        return None

    with open(file_path, "r") as file:
        data = json.load(file)

    return data
    