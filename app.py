import os

from src.drive_service import (
    get_drive_service,
    list_root_folders,
    list_shared_folders
)

from src.quality_ranker import analyze_folder
from src.analysis_storage import save_analysis, load_analysis

from src.candidate_selector import (
    select_candidates,
    group_duplicates,
    keep_sharpest
)

from src.selection_storage import save_selection


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():

    clear()

    print("============================")
    print("AI Event Photo Finder")
    print("============================\n")

    service = get_drive_service()

    print("Connected to Google Drive ✓\n")

    print("1. My Drive")
    print("2. Shared With Me")

    choice = int(input("\nChoose: "))

    clear()

    if choice == 1:
        folders = list_root_folders(service)
    elif choice == 2:
        folders = list_shared_folders(service)
    else:
        print("Invalid choice.")
        return

    print("Select Folder")
    print("-------------")

    for index, folder in enumerate(folders, start=1):
        print(f"{index}. {folder['name']}")

    choice = int(input("\nChoose a Folder: "))

    clear()

    folder = folders[choice - 1]

    folder_id = folder["id"]
    folder_name = folder["name"]

    print(f"Folder : {folder_name}\n")

    analysis = load_analysis(folder_id)

    if analysis is None:

        print("No cached analysis found.")
        print("Analyzing images...\n")

        results = analyze_folder(
            service,
            folder_id
        )

        save_analysis(
            folder_name,
            folder_id,
            results
        )

        print("\nAnalysis saved successfully.\n")

    else:

        print("Analysis cache found.\n")

        print("1. Load existing analysis")
        print("2. Re-analyze")

        choice = int(input("\nChoose: "))

        clear()

        if choice == 1:

            results = analysis["images"]

            print("Loaded cached analysis.\n")

        elif choice == 2:

            print("Re-analyzing images...\n")

            results = analyze_folder(
                service,
                folder_id
            )

            save_analysis(
                folder_name,
                folder_id,
                results
            )

            print("\nAnalysis updated successfully.\n")

        else:

            print("Invalid choice.")
            return

    candidates = select_candidates(results)

    groups = group_duplicates(candidates)

    best_images = keep_sharpest(groups)

    clear()

    print("============================")
    print("Analysis Summary")
    print("============================\n")

    print(f"Total Images      : {len(results)}")
    print(f"After Blur Filter : {len(candidates)}")
    print(f"Duplicate Groups  : {len(groups)}")
    print(f"Best Images       : {len(best_images)}")

    save_selection(
    folder_name,
    folder_id,
    best_images
    )
    print("\nSelection saved successfully.")


if __name__ == "__main__":
    main()