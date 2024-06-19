import cv2
import numpy as np


class BoxFilter:
    __slots__ = ['path', 'size']

    def __init__(self, path: str, size: int):
        self.path = path
        self.size = size

    def kernel(self):
        return np.ones((self.size, self.size), np.float32) / 9.0

    def converter(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.filter2D(gray, -1, self.kernel())

    def show_image(self):
        cv2.imshow('Box filter', self.converter())
        cv2.waitKey(0)
        cv2.destroyAllWindows()
