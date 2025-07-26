import numpy as np

array1 = np.array([[4,7],[2,6]])

array1_transpose = np.transpose(array1) # transposes the matrix, meaning rows become columns and columns become rows.
array2_transpose = array1.T # .T is shorthand syntax for taking the transpose in NumPy. It's equivalent to np.transpose(array1)

print(array1)
'''
[[4 7]
 [2 6]]
'''

print(array1_transpose)
'''
[[4 2]
 [7 6]]
'''

print(array2_transpose)
'''
[[4 2]
 [7 6]]
'''