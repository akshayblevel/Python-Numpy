import numpy as np

a = np.array([[14, 10], [16, 11], [17,10]])

print(a)
print(type(a))

row, col = a.shape

print("row: ", row)
print("col: ", col)

'''
OUTPUT:
[[14 10]
 [16 11]
 [17 10]]
<class 'numpy.ndarray'>
row:  3
col:  2
'''
