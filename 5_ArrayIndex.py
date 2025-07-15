import numpy as np

print("Integer Array")
intArray = np.array([14, 10, 81])
print(intArray.shape)  # prints: (3,)
print(intArray.dtype)  # prints: int64
print(intArray)  # prints: [14, 10, 81]

print("Float Array")
floatArray = np.array([[14.10, 16.11, 17.10], [1.3, 4.8, 13.09]])
print(floatArray.shape)  # prints: (2, 3)
print(floatArray.dtype)  # prints: float64
print(floatArray) # prints: [[14.10, 16.11, 17.10], [1.3, 4.8, 13.09]]

print("Array Index")
print(intArray[0], intArray[1], intArray[2])  # prints: 14, 10, 81
print(floatArray[0, 0], floatArray[0, 1], floatArray[1, 0])  # prints: 14.1, 16.11, 1.3

print("Update Array Index")
intArray[0] = 17
print(intArray)  # prints: [17, 10, 81]

floatArray[0, 0] = 31.12
print(floatArray)  # prints: [[31.12, 16.11, 17.10], [1.3, 4.8, 13.09]]