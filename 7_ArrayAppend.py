import numpy as np

intArray = np.array([14, 10, 81])
print("IntArray",intArray) # IntArray [14 10 81]

negativeArray = np.array([-14, -10, -81])
addIntNegative = intArray + negativeArray
print("AddIntNegative (after append)...",addIntNegative) # AddIntNegative (after append)... [0 0 0]

addValueIntArray = intArray + 5
print("AddValueIntArray (after plus operation)...", addValueIntArray) # AddValueIntArray (after plus operation)... [19 15 86]
print("IntArray...", intArray) # IntArray... [14 10 81]

appendUsingFunc = np.append(intArray, 10)
print("AppendUsingFunc", appendUsingFunc) # AppendUsingFunc [14 10 81 10]
