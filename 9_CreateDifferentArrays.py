import numpy as np

#Create a 3x3 array of all zeros.
allZeroArray = np.zeros((3, 3))
print(allZeroArray)
'''
    [[0. 0. 0.]
    [0. 0. 0.]
    [0. 0. 0.]]
'''

#Create a 2x2 array of all ones.
allOnesArray = np.ones((2,2))
print(allOnesArray)
'''
    [[1. 1.]
    [1. 1.]]
'''

#Create a 3x3 identity matrix. 
identityMatrix = np.eye(3)
print(identityMatrix)
'''
    [[1. 0. 0.]
    [0. 1. 0.]
    [0. 0. 1.]]
'''

#Create an array of 15 random numbers from 0 to 100.
randomArray = np.random.randint(0, 100, 15)
print(randomArray)
'''
[43 95 76 97 38 91 55 92 73 44 34 78 17 31 17]
'''