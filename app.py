from src.drive_service import get_drive_service
from src.drive_service import list_root_folders
from src.drive_service import list_images
from src.drive_service import list_shared_folders
from src.image_loader import download_image
import cv2
from src.blur_detector import detect_blur
import time
from src.duplicate_detector import average_hash
from src.duplicate_detector import compare_hashes

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

    image1 = download_image(service, images[0]["id"])
    image2 = download_image(service, images[0]["id"])

    hash1 = average_hash(image1)
    hash2 = average_hash(image2)

    difference = compare_hashes(
    hash1,
    hash2
    )

    print(difference)
        




if __name__ == "__main__":
    main()