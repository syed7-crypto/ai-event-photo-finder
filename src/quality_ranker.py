from src.duplicate_detector import average_hash
from src.blur_detector import detect_blur
from src.image_loader import download_image
from src.drive_service import list_images

def analyze_image(image, image_info):

    analysis = {
        "id": image_info["id"],
        "name": image_info["name"],
        "blur_score": detect_blur(image),
        "hash": average_hash(image).tolist()
    }

    return analysis

def analyze_folder(service, folder_id):

    images= list_images(service, folder_id)
    results = []
        
    print(f"Total images: {len(images)}")

    for image_info in images:

        print("Processing:", image_info["name"])

        if image_info["name"].lower().endswith(".dng"):
            print(f"Skipping {image_info['name']} (RAW image)")
            continue

        image = download_image(
            service,
            image_info["id"]
        )

        if image is None:
            print(f"Skipping {image_info['name']} (Unsupported format)")
            continue

        result = analyze_image(
            image,
            image_info
        )

        print("Analyzed:", result["name"])

        results.append(result)

    print("Finished")
    print("Results:", len(results))

    return results
