import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the pixel values of an image array.

    Args:
        array (np.ndarray): Input image array of shape
        (height, width, channels).

    Returns:
        np.ndarray: Inverted image array.
    """
    array = array.astype(np.uint8)
    height, width, channels = array.shape
    inverted_array = np.empty((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                inverted_array[i, j, k] = 255 - array[i, j, k]
    plt.imshow(inverted_array)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Extracts the red channel from an image array.

    Args:
        array (np.ndarray): Input image array of shape
        (height, width, channels).

    Returns:
        np.ndarray: Image array with only the red channel.
    """
    array = array.astype(np.uint8)
    height, width, channels = array.shape
    red_array = np.empty((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                if k != 0:
                    red_array[i, j, k] = 0
    plt.imshow(red_array)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Extracts the green channel from an image array.

    Args:
        array (np.ndarray): Input image array of shape
        (height, width, channels).

    Returns:
        np.ndarray: Image array with only the green channel.
    """
    array = array.astype(np.uint8)
    height, width, channels = array.shape
    green_array = np.empty((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                if k != 1:
                    green_array[i, j, k] = 0
    plt.imshow(green_array)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Extracts the blue channel from an image array.

    Args:
        array (np.ndarray): Input image array of shape
        (height, width, channels).

    Returns:
        np.ndarray: Image array with only the blue channel.
    """
    array = array.astype(np.uint8)
    height, width, channels = array.shape
    blue_array = np.empty((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                if k != 2:
                    blue_array[i, j, k] = 0
    plt.imshow(blue_array)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts an image array to grayscale.

    Args:
        array (np.ndarray): Input image array of shape
        (height, width, channels).

    Returns:
        np.ndarray: Grayscale image array.
    """
    array = array.astype(np.uint16)
    height, width, channels = array.shape
    grey_array = np.empty((height, width, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            grey_value = (array[i, j, 0] + array[i, j, 1] +
                          array[i, j, 2]) // 3
            grey_array[i, j, 0] = grey_value
            grey_array[i, j, 1] = grey_value
            grey_array[i, j, 2] = grey_value
    plt.imshow(grey_array)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    return grey_array
