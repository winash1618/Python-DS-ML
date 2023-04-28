"""
Manipulation of loaded image via numpy arrays, broadcasting.
"""

import numpy as np

class ColorFilter:
    """
    You have some restrictions on the authorized methods and operators for each filter
    method in class ColorFilter:
    • invert:
        ◦ Authorized functions: .copy.
        ◦ Authorized operators: +,-,=.
    • to_blue:
        ◦ Authorized functions: .copy, .zeros,.shape,.dstack.
        ◦ Authorized operators: =.
    • to_green:
        ◦ Authorized functions: .copy.
        ◦ Authorized operators: *, =.
    • to_red:
        ◦ Authorized functions: .copy, .to_green,.to_blue.
        ◦ Authorized operators: -,+, =.
    • to_celluloid(array):
        ◦ Authorized functions: .copy, .arange,.linspace, .min, .max.
        ◦ Authorized operators: =, <=, >, & (or and).
    • to_grayscale:
        ◦ Authorized functions: .sum,.shape,.reshape,.broadcast_to,.as_type.
        ◦ Authorized operators: *,/, =.
    """
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        import numpy as np

        # create a 3D numpy array
        arr = np.array([
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
        ])
        
        # select the first row
        print(arr[0, :, :])  # outputs: [[1 2 3], [4 5 6], [7 8 9]]
        
        # select the second column
        print(arr[:, 1, :])  # outputs: [[4 5 6], [13 14 15], [22 23 24]]
        
        # select the first two color channels (R, G)
        img = np.array([
            [[255, 128, 0, 255], [0, 255, 128, 255], [128, 0, 255, 255]],
            [[255, 255, 0, 128], [255, 0, 255, 128], [0, 255, 255, 128]],
            [[128, 128, 128, 0], [64, 64, 64, 0], [0, 0, 0, 0]]
        ], dtype=np.uint8)
        
        print(img[:, :, :2])
        # outputs: [[[255 128], [0 255], [128 0]], [[255 255], [255 0], [0 255]], [[128 128], [64 64], [0 0]]]
        """
        result = np.copy(array)
        new_array = 255 - result[:, :, :3]
        result[:, :, :3] = new_array
        return result
    
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        result = np.zeros(np.shape(array), dtype=np.uint8)
        result[:, :, 2] = array[:, :, 2]
        result[:, :, 3] = array[:, :, 3]
        return (result)

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        result = np.copy(array)
        result[:, :, 0] -= array[:, :, 0]
        result[:, :, 2] -= array[:, :, 2]
        return (result)
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        result = np.copy(array)
        result[:, :, :3] -= self.to_green(array)[:, :, :3] + self.to_blue(array)[:, :, :3]
        return (result)
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        
    
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
    