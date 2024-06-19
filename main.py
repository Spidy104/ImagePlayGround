from Morphological_Operation.TopHat import TopHatOp
path: str = 'images//Lenna_(test_image).png'

if __name__ == '__main__':
    print('Entry point to the whole code')
    g = TopHatOp(path, 3)
    g.apply()

