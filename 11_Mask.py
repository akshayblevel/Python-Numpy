import numpy as np

intArray = np.array([11, 10, 19, 81, 17])

# Using a mask to get values greater than 10
mask = intArray > 10
print(mask) # [ True False  True  True  True]
print(intArray[mask])   # [11 19 81 17]
print("intArray and mask shares same memory?...",np.shares_memory(intArray,mask)) # intArray and mask shares same memory?... False
print("mask base...", mask.base) # mask base... None

b = np.array([1,1,1,2,2])
print(intArray[b]) #  [10 10 10 19 19] # fancy indexing — using integer indices to pick elements from intArray

# Count the number of elements greater than 10
print(np.count_nonzero(mask)) # 4

# Masking can be used directly in expressions
print(intArray[intArray > 10]) # [11 19 81 17]