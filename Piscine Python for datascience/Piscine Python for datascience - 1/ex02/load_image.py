from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    try:
        image = Image.open(path)
        
        image_array = np.array(image)
        
        print("The shape of image is: ", image_array.shape)
        
        image.close()

        return image_array
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None