import numpy as np

intArray = np.array([14, 10, 81, 16, 11, 84])

array1, array2 = np.split(intArray, 2)

print(array1)  # Outputs: [14 10 81]
print(array2)  # Outputs: [16 11 84]