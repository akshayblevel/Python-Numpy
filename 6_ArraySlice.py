import numpy as np

oneArray = np.array([14, 10, 81])
twoArray = np.array([[14.10, 16.11, 17.10], [1.3, 4.8, 13.09]])

oneSlicedArray = oneArray[1:3]  
print(oneSlicedArray)   # [10 81]
print(type(oneSlicedArray)) # <class 'numpy.ndarray'>
print(oneSlicedArray.shape) # (2,)

twoSlicedArray = twoArray[0:1, 1:3] 
print(twoSlicedArray) # [[16.11 17.1 ]]
print(twoSlicedArray.shape) # (1, 2)