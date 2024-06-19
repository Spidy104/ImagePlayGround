import cv2
import numpy as np


class PrewittMask:
    __slots__ = ['path']

    def __init__(self, path: str):
        self.path = path

    def apply(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply Prewitt operator to detect horizontal edges
        prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        edges_x = cv2.filter2D(gray, -1, prewitt_x)

        # Apply Prewitt operator to detect vertical edges
        prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        edges_y = cv2.filter2D(gray, -1, prewitt_y)

        # Combine the horizontal and vertical edges
        edges = np.sqrt(edges_x ** 2 + edges_y ** 2)
        cv2.imshow('Prewitt Edge Detection', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
