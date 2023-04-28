from ImageProcessor import ImageProcessor
import numpy as np
imp = ImageProcessor()
arr = imp.load("assets/elon_canaGAN.png")
# Output :
# Loading image of dimensions 200 x 200
img = np.array([
    [[255, 128, 0, 255], [0, 255, 128, 255], [128, 0, 255, 255]],
    [[255, 255, 0, 128], [255, 0, 255, 128], [0, 255, 255, 128]],
    [[128, 128, 128, 0], [64, 64, 64, 0], [0, 0, 0, 0]]
], dtype=np.uint8)
from ColorFilter import ColorFilter
cf = ColorFilter()
# np.set_printoptions(threshold=np.inf)
# print(cf.invert(img))
# imp.display(cf.invert(arr))
# print(cf.to_green(img))
# imp.display(cf.to_green(arr))
imp.display(cf.to_red(arr))
# print(cf.to_blue(img))
# imp.display(cf.to_blue(arr))
# cf.to_celluloid(arr)
# cf.to_grayscale(arr, 'm')
# cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5])