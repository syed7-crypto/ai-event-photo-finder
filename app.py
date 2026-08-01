from src.drive_service import get_drive_service
from src.drive_service import list_root_folders
from src.drive_service import list_images
from src.drive_service import list_shared_folders

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
    for index, image in enumerate(images, start=1):
            print(index,".", image["name"])




if __name__ == "__main__":
    main()