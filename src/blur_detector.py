import cv2

def detect_blur(image):

    gray_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    laplacian = cv2.Laplacian(
        gray_image,
        cv2.CV_64F
    )

    score = laplacian.var()

    return score