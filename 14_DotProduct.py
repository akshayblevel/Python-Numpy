import numpy as np

array1 = np.array([[14,10],[16,11]])
array2 = np.array([[17,10],[17,11]])

print(array1)
print(array2)

dotProductArray = array1.dot(array2)

print(dotProductArray)

'''
Compute each element in dotProductArray = array1.dot(array2):
c[0][0] = (14×17 + 10×17) = 238 + 170 = 408
c[0][1] = (14×10 + 10×11) = 140 + 110 = 250

c[1][0] = (16×17 + 11×17) = 272 + 187 = 459
c[1][1] = (16×10 + 11×11) = 160 + 121 = 281

OUTPUT:
[[14 10]
 [16 11]]

[[17 10]
 [17 11]]

 [[408 250]
 [459 281]]
'''