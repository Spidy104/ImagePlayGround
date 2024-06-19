import cv2
import numpy as np


class Laplacian_Edge:
    __slots__ = ['path', 'kernel_size']

    def __init__(self, path: str, kernel_size: int):
        self.path = path
        self.kernel_size = kernel_size

    def apply(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (self.kernel_size, self.kernel_size), 0)
        laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
        edges = np.uint8(np.absolute(laplacian))
        cv2.imshow('Laplacian Edge Detection', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
