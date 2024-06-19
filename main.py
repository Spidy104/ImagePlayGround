from spatial_filters.gaussian_filter_experimental import Gaussian
path: str = 'images//Lenna_(test_image).png'

if __name__ == '__main__':
    print('Entry point to the whole code')
    g = Gaussian(path, 3, 1.5)
    g.show_image()

