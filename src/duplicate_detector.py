import cv2
import numpy as np

def average_hash(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    small_image = cv2.resize(
        gray,
        (8, 8)
    )

    average = small_image.mean()

    hash_array = small_image > average

    return hash_array.flatten()

def compare_hashes(hash1, hash2):

    difference = np.count_nonzero(
        hash1 != hash2
    )

    return difference