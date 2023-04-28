"""
Test for the ScrapBooker class
"""

import numpy as np
from ScrapBooker import ScrapBooker
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))
#Output :
# [[ 5]
#  [10]
#  [15]]
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2,3,0))
#Output :
# [['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']
#  ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I']]
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))
#Output :
# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
# [1, 2, 3, 1, 2, 3, 1, 2, 3],
# [1, 2, 3, 1, 2, 3, 1, 2, 3]])
arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.mosaic(arr4, (2, 3)))
# [[1 2 3 1 2 3 1 2 3]
#  [1 2 3 1 2 3 1 2 3]
#  [1 2 3 1 2 3 1 2 3]
#  [1 2 3 1 2 3 1 2 3]
#  [1 2 3 1 2 3 1 2 3]
#  [1 2 3 1 2 3 1 2 3]]