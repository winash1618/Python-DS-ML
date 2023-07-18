from PIL import Image
from load_image import ft_load
import numpy as np

try:
    image_array = ft_load("landscape.jpg")
    if image_array is None:
        print("Error: unable to load the image")
        exit()
    zoom_factor = 3
    # Determine new dimensions based on zoom factor
    height, width, _ = image_array.shape
    new_height = int(height * zoom_factor)
    new_width = int(width * zoom_factor)

    # Convert the image array to uint8 data type
    image_array = image_array.astype(np.uint8)

    # Convert the NumPy array to a PIL Image object
    image = Image.fromarray(image_array)

    # Resize the image using the new dimensions
    zoomed_image = image.resize((new_width, new_height), Image.BILINEAR)

    # Display the zoomed image
    zoomed_image.show()

except Exception as e:
    print(f"An error occurred while zooming the image: {e}")
