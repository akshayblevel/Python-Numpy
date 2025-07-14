import numpy as np

def multiply(i, j):
    return i * j

array = np.fromfunction(multiply, (4, 5), dtype=int)

print(array)	

'''
MULTIPLY ROW INDEX WITH COLUMN INDEX
OUTPUT:
[[ 0  0  0  0  0]
 [ 0  1  2  3  4]
 [ 0  2  4  6  8]
 [ 0  3  6  9 12]]
'''