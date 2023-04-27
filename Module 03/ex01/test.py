"""
test for ImageProcessor
"""
from ImageProcessor import ImageProcessor
imp = ImageProcessor()
image = imp.load("./png.png")
# Output :
# Loading image of dimensions 200 x 200
imp.display(image)

arr = imp.load("non_existing_file.png")
print(arr)

arr = imp.load("empty_file.png")
