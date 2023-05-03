"""
Basic manipulation of image via matplotlib library.
"""

import matplotlib.pyplot as plt
from PIL import Image, UnidentifiedImageError
import numpy as np
import matplotlib
matplotlib.use('Agg')

class ImageProcessor(object):
    """
    class for image processing functionality
    """
    def load(self, path):
        """
        opens the PNG file specified by the path argument and returns an
        array with the RGB values of the pixels image. It must display a message specifying
        the dimensions of the image (e.g. 340 x 500).
        """
        try:
            with open(path, 'rb') as file:
                try:
                    img = Image.open(file)
                except UnidentifiedImageError as err:
                    print(err)
                    return None
                img_array = np.array(img)
                height, width = img.size
        except FileNotFoundError as err:
                print(err)
                return None
        print(f"Loading image of dimensions /{ {height}, {width} }")
        return img_array

    def display(self, array):
        """
        takes a numpy array as an argument and displays the corresponding RGB image
        """
        plt.imshow(array, cmap='gray')
        plt.show()
        plt.savefig('image.png')
