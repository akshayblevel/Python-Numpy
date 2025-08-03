import numpy as np

array1 = np.array([[14, 10, 81], [16, 11, 84]])
flattenArray = array1.flatten()
print(flattenArray)  # Outputs: [14 10 81 16 11 84]
flattenArray[0] = 100
print(array1)

'''
OUTPUT:
[[14 10 81]
 [16 11 84]]

Returns: A flattened copy of the original array.
Memory: Always copies data — less efficient.
Changes in original: Will not affect the original array.
'''

ravelArray = array1.ravel()
print(ravelArray)  # Outputs: [14 10 81 16 11 84]
ravelArray[1] = 101
print(array1)

'''
OUTPUT:
[[ 14 101  81]
 [ 16  11  84]]

Returns: A flattened view of the original array whenever possible (i.e., no data copy).
Memory: Does not copy data if not needed — efficient.
Changes in original: If a view is returned, changes in the raveled array may affect the original.
'''