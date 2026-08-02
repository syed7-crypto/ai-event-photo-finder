from src.drive_service import get_drive_service
from src.drive_service import list_root_folders
from src.drive_service import list_shared_folders
from src.quality_ranker import analyze_folder
from src.analysis_storage import save_analysis, load_analysis

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
    folder_name=folder["name"]

    analysis = load_analysis(folder_id)

    if analysis is None:
        results = analyze_folder(service, folder_id)
        save_analysis(folder_name,folder_id,results)
        print("Analysis saved successfully!")

    else:
        print("1. Load")
        print("2. Re-analyze")
        choice = int(input("Choose: "))
        if choice == 1:
            results = analysis["images"]
            print("Loaded cached analysis.")
            print("Results:", len(results))
        else:
            results = analyze_folder(service, folder_id)
            save_analysis(folder_name,folder_id,results)
            print("Analysis saved successfully!")

        
if __name__ == "__main__":
    main()