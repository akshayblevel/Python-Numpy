import numpy as np

intArray = np.array([14, 10, 81])

copyArray = intArray.copy()
print("intArray & copyArray shares same memory?...",np.shares_memory(intArray,copyArray)) # intArray & copyArray shares same memory?... False
print("copyArray...",copyArray) # copyArray... [14 10 81]

print("base of intArray...",intArray.base)  # base of intArray... None
print("base of copyArray...",copyArray.base)    # base of copyArray... None    

intArray[2] = 91
print("intArray (after modification)...", intArray) # intArray (after modification)... [14 10 91]
print("copyArray (after modification of intArray)...", copyArray) # copyArray (after modification of intArray)... [14 10 81]

copyArray[0] = 17
print("copyArrary (after modification)...",copyArray)   # copyArrary (after modification)... [17 10 81]
print("intArray (after modification of copyArray)...", intArray) # intArray (after modification of copyArray)... [14 10 91]

copyArray.flags.writeable = False
# copyArray[0] = 14   # ValueError: assignment destination is read-only
print("copyArray (after making read only)...",copyArray)

intArray[1] = 11
print("intArray (after modification)...",intArray) # intArray (after modification)... [14 11 91]
print("copyArray (after modification of intArray)...",copyArray) # copyArray (after modification of intArray)... [17 10 81]

