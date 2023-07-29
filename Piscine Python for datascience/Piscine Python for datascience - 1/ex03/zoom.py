import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import ft_load


def zoom_image(image_array, zoom_factor):
    """Zoom an image by a specified factor using PIL.

    Args:
        image_array (numpy.ndarray): The image represented as a NumPy array.
        zoom_factor (float): The factor by which to zoom the image.

    Returns:
        PIL.Image.Image: The zoomed image.
    """
    height, width, channels = image_array.shape
    new_height = int(height * zoom_factor)
    new_width = int(width * zoom_factor)

    image_array = image_array.astype(np.uint8)

    image = Image.fromarray(image_array)

    zoomed_image = image.resize((new_width, new_height), Image.BILINEAR)

    return zoomed_image


def main():
    try:
        image_path = "landscape.jpg"
        image_array = ft_load(image_path)

        if image_array is None:
            print("Error: Unable to load the image")
            exit()

        zoom_factor = 3
        zoomed_image = zoom_image(image_array, zoom_factor)

        width, height = zoomed_image.size
        print(f"Image size: {width} pixels (width) x {height} pixels (height)")

        channels = len(zoomed_image.getbands())
        print(f"Number of channels: {channels}")

        plt.imshow(zoomed_image)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    except Exception as e:
        print(f"An error occurred while processing the image: {e}")


if __name__ == "__main__":
    main()
