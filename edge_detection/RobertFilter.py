import cv2
import numpy as np


class RobertFilter:
    __slots__ = ['path']

    def __init__(self, path: str):
        self.path = path

    def apply(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Define the Roberts Cross kernel
        roberts_cross_x = np.array([[1, 0], [0, -1]])
        roberts_cross_y = np.array([[0, 1], [-1, 0]])

        # Apply the Roberts Cross operator
        grad_x = cv2.filter2D(gray, -1, roberts_cross_x)
        grad_y = cv2.filter2D(gray, -1, roberts_cross_y)

        # Calculate the gradient magnitude
        grad_magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)

        # Normalize the gradient magnitude
        grad_magnitude = cv2.normalize(grad_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imshow('Roberts Cross Edge Detection', grad_magnitude)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
