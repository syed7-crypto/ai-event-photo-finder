import io

import cv2
import numpy as np

from googleapiclient.http import MediaIoBaseDownload


def download_image(service, file_id):

    buffer = io.BytesIO()

    request = service.files().get_media(
        fileId=file_id
    )

    downloader = MediaIoBaseDownload(
        buffer,
        request
    )

    done = False

    while not done:
        status, done = downloader.next_chunk()

    buffer.seek(0)

    image_bytes = buffer.getvalue()

    image_array = np.frombuffer(
        image_bytes,
        dtype=np.uint8
    )

    image = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )

    return image