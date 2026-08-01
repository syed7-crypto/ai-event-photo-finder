from src.drive_service import get_drive_service
from src.drive_service import list_root_folders
from src.drive_service import list_images
from src.drive_service import list_shared_folders
from src.image_loader import download_image
import cv2
from src.blur_detector import detect_blur
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

    for image_info in images:

        download_start = time.time()

        image = download_image(
            service,
            image_info["id"]
        )

        download_end = time.time()

        blur_start = time.time()

        score = detect_blur(image)

        blur_end = time.time()

        print(f"{image_info['name']}")
        print(f"Blur Score : {score:.2f}")
        print(f"Download   : {download_end - download_start:.2f} sec")
        print(f"Detection  : {blur_end - blur_start:.4f} sec")
        print("-" * 40)
        




if __name__ == "__main__":
    main()