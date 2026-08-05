from src.duplicate_detector import compare_hashes
BLUR_THRESHOLD=3000
HASH_THRESHOLD=9

def select_candidates(results):
    candidates=[]
    for image in results:
        if image["blur_score"]>BLUR_THRESHOLD:
            candidates.append(image)
    return candidates

def group_duplicates(candidates):
    groups = []
    used = set()
    for i, image in enumerate(candidates):
        if i in used:
            continue
        group = [image]
        used.add(i)
        for j in range(i + 1, len(candidates)):
            if j in used:
                continue
            distance =compare_hashes(
                image["hash"],
                candidates[j]["hash"]
            )
            if distance <= HASH_THRESHOLD:
                group.append(candidates[j])
                used.add(j)
        groups.append(group)
    return groups

def keep_sharpest(groups):
    best_images = []
    
    for group in groups:
        sharpest_image = group[0]
        highest_score = group[0]["blur_score"]

        for image in group:
            if image["blur_score"] > highest_score:
                highest_score = image["blur_score"]
                sharpest_image = image
                
        best_images.append(sharpest_image)
        
    return best_images

