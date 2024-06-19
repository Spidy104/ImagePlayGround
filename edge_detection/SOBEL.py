import cv2


class SobelFilter:
    __slots__ = ['path', 'kernel_size']

    def __init__(self, path: str, kernel_size: int):
        self.path = path
        self.kernel_size = kernel_size

    def apply(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grad_x = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=self.kernel_size)

        # Apply Sobel operator to detect vertical edges
        grad_y = cv2.Sobel(gray, cv2.CV_8U, 0, 1, ksize=self.kernel_size)

        # Calculate the gradient magnitude
        grad = cv2.magnitude(grad_x, grad_y)

        # Threshold the gradient magnitude
        _, thresh = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow('Sobel Edge Detection', thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
