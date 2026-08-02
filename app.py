from src.drive_service import get_drive_service
from src.drive_service import list_root_folders
from src.drive_service import list_images
from src.drive_service import list_shared_folders
from src.image_loader import download_image
from src.quality_ranker import analyze_image
from src.analysis_storage import save_analysis
import cv2
import time

def main():
    print("============================\nAI Event Photo Finder\n============================")
    service = get_drive_service()

    print("Connected successfully!")

    print("1. My Drive\n\n2. Shared With Me")
    choice=int(input("Choose: "))
    if choice==1:
        folders = list_root_folders(service)
    elif choice==2:
        folders = list_shared_folders(service)
    else:
        print("invalid choice")

    for index, folder in enumerate(folders, start=1):
        print(index,".", folder["name"])
    choice = int(input("Choose a Folder: "))

    folder = folders[choice - 1]
    folder_id=folder["id"]

    images= list_images(service, folder_id)
    results = []
        
    print(f"Total images: {len(images)}")

    for image_info in images:

        print("Processing:", image_info["name"])

        if image_info["name"].lower().endswith(".dng"):
            print(f"Skipping {image_info['name']} (RAW image)")
            continue

        image = download_image(
            service,
            image_info["id"]
        )

        if image is None:
            print(f"Skipping {image_info['name']} (Unsupported format)")
            continue

        result = analyze_image(
            image,
            image_info
        )

        print("Analyzed:", result["name"])

        results.append(result)

    print("Finished")
    print("Results:", len(results))
    save_analysis(
    folder["name"],
    folder["id"],
    results
    )

    print("Analysis saved successfully!")
