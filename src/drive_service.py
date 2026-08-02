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

def list_root_folders(service):

    results = service.files().list(
        q="mimeType='application/vnd.google-apps.folder' and 'root' in parents",
        pageSize=20,
        fields="files(id, name)"
    ).execute()

    return results.get("files", [])

def list_shared_folders(service):
    
    results = service.files().list(
        q="sharedWithMe and mimeType='application/vnd.google-apps.folder' and trashed=false",
        pageSize=20,
        fields="files(id, name)"
    ).execute()

    return results.get("files", [])

def list_images(service, folder_id):
    query = (
    f"'{folder_id}' in parents "
    "and mimeType contains 'image/' "
    "and trashed = false"
    )
    results = service.files().list(
            q=query,
            pageSize=1000,
            fields="files(id, name, mimeType, thumbnailLink)"
        ).execute()
    return results.get("files", [])