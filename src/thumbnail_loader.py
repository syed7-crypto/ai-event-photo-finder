# We analyze Google Drive thumbnails instead of full-resolution images.
# This significantly reduces download time while preserving enough detail
# for blur detection and average-hash duplicate detection.

import requests
import numpy as np
import cv2


def download_thumbnail(image_info):

    url = image_info.get("thumbnailLink")

    if not url:
        return None

    response = requests.get(url)

    if response.status_code != 200:
        return None

    image_bytes = response.content

    image_array = np.frombuffer(
        image_bytes,
        dtype=np.uint8
    )

    image = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )

    return image