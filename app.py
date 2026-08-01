from src.drive_service import get_drive_service


def main():
    service = get_drive_service()

    print("Connected successfully!")

    results = service.files().list(
    q="mimeType='application/vnd.google-apps.folder' and 'root' in parents",
    pageSize=20,
    fields="files(id, name)"
    ).execute()

    files = results.get("files", [])

    for index, file in enumerate(files, start=1):
        print(index, file["name"])


if __name__ == "__main__":
    main()