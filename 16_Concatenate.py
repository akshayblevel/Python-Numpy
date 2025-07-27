import numpy as np

array1 = np.array([14, 10, 81])
array2 = np.array([17, 10, 17])

cArray = np.concatenate([array1, array2])

print(cArray)  # Outputs: [14 10 81 17 10 17]