import cv2
import numpy as np


class TopHatOp:

    def __init__(self, path: str, kernel_size: int) -> None:
        self.path = path
        self.kernel_size = kernel_size

    def apply(self):
        img = cv2.imread(self.path)
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Define the structuring element
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        # Apply the filtering operation
        opening = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
        cv2.imshow('TopHat', opening)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
