from src.drive_service import get_drive_service


def main():
    service = get_drive_service()

    print("Connected successfully!")

    results = service.files().list(
        pageSize=10,
        fields="files(id, name)"
    ).execute()

    files = results.get("files", [])

    for file in files:
        print(file["name"])


if __name__ == "__main__":
    main()