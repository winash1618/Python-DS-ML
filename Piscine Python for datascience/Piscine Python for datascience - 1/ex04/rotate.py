from PIL import Image
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

try:
    image_array = ft_load("landscape.jpg")
    if image_array is None:
        print("Error: unable to load the image")
        exit()
    
    image_array = image_array.astype(np.uint8)
    square_image = image_array[0: 400, 0: 400, :]  # Extract the square region
    height, width, channels = square_image.shape
    
    rotated_image = np.empty((width, height, channels), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(channels):
                rotated_image[j, i, k] = square_image[i, j, k]
    
    height, width, channels = rotated_image.shape
    print(f"Image size: {width} pixels (width) x {height} pixels (height)")
    print(f"Number of channels: {channels}")
    
    plt.imshow(rotated_image)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
except Exception as e:
    print(f"An error occurred while processing the image: {e}")
