import cv2


class MeanFilter:
    __slots__ = ['path', 'kernel_size']

    def __init__(self, path: str, kernel_size: int) -> None:
        self.path = path
        self.kernel_size = kernel_size

    def apply(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.blur(gray, (self.kernel_size, self.kernel_size))

    def show_image(self):
        cv2.imshow('Mean Filter', self.apply())
        cv2.waitKey(0)
        cv2.destroyAllWindows()
