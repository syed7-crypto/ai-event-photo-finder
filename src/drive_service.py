from googleapiclient.discovery import build

from src.drive_auth import authenticate

def get_drive_service():
    creds = authenticate()

    service = build(
        "drive",
        "v3",
        credentials=creds
    )

    return service