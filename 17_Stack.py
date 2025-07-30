import numpy as np

array1 = np.array([[14, 10],
              [16, 11]])
array2 = np.array([[17, 10]])

result = np.vstack((array1, array2))
print(result)

'''
OUTPUT:
[[14 10] 
 [16 11] 
 [17 10]]
'''

array2 = np.array([[17],
              [10]])

result = np.hstack((array1, array2))
print(result)

'''
OUTPUT:
[[14 10 17]
 [16 11 10]]
'''