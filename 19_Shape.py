import numpy as np

array1 = np.array([14, 10, 81, 16, 11, 84])

print("array1 :: ",array1)
print("array1.shape ",array1.shape)

'''
OUTPUT:
array1 ::  [14 10 81 16 11 84]
array1.shape  (6,)
'''

array2 = np.reshape(array1, (2, 3))

print("array2 :: ",array2)
print("array2.shape ",array2.shape)

'''
OUTPUT:
array2 ::  [[14 10 81]
 [16 11 84]]
array2.shape  (2, 3)
'''