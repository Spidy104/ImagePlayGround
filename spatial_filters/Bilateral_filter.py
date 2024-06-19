import cv2


class Bilateral:

    def __init__(self, path: str, kernel_size: int, space_sensitivity: int = 50, color_intensity: int = 50):
        self.path = path
        self.kernel_size = kernel_size
        self.space_sensitivity = space_sensitivity
        self.color_sensitivity = color_intensity

    def show_image(self):
        img = cv2.imread(self.path)
        bilateral = cv2.bilateralFilter(img, self.kernel_size, self.color_sensitivity, self.space_sensitivity)
        cv2.imshow('Bilateral Filter', bilateral)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
