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

    rotated_image = square_image.transpose((1, 0, 2))
    
    height, width, channels = rotated_image.shape
    print(f"Image size: {width} pixels (width) x {height} pixels (height)")
    print(f"Number of channels: {channels}")
    
    plt.imshow(rotated_image)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    
except Exception as e:
    print(f"An error occurred while processing the image: {e}")
