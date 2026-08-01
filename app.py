from src.drive_service import get_drive_service
from src.drive_service import list_root_folders
from src.drive_service import list_images

def main():
    service = get_drive_service()

    print("Connected successfully!")

    folders = list_root_folders(service)

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