import cv2
import matplotlib.pyplot as plt
import numpy as np


class Gaussian:

    def __init__(self, path: str, kernel_size: int, deviation: float | int):
        self.path = path
        self.kernel_size = kernel_size
        self.deviation = deviation

    def kernel(self):
        kernel_op = np.zeros((self.kernel_size, self.kernel_size))
        for i in range(self.kernel_size):
            for j in range(self.kernel_size):
                x = i - self.kernel_size // 2
                y = j - self.kernel_size // 2
                kernel_op[i, j] = np.exp(-(x ** 2 + y ** 2) / (2 * self.deviation ** 2)) / (
                        2 * np.pi * self.deviation ** 2)
        kernel_op /= np.sum(kernel_op)
        return kernel_op

    def apply(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        filtered = np.zeros_like(gray)
        for i in range(1, gray.shape[0] - 1):
            for j in range(1, gray.shape[1] - 1):
                roi = gray[i - self.kernel_size // 2:i + self.kernel_size // 2 + 1,
                      j - self.kernel_size // 2:j + self.kernel_size // 2 + 1]
                filtered[i, j] = np.sum(roi * self.kernel())
        return filtered

    def show_image(self):
        plt.imshow(self.apply(), cmap='gray')
        plt.show()
