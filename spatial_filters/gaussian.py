import cv2


class Gaussian:
    __slots__ = ['path', 'kernel_size']

    def __init__(self, path: str, kernel_size: int):
        self.path = path
        self.kernel_size = kernel_size

    def show_image(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (self.kernel_size, self.kernel_size), 0)
        cv2.imshow('Gaussian Filter', blurred)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
