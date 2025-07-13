import numpy as np

start = 0
end = 12
step = 3

arangeResult = np.arange(start, end, step) 
print(arangeResult)

'''
OUTPUT:
[0 3 6 9]
'''

'''
FencePost Problem
np.arange omits the final post - hence 12 is missing in output
np.linespace is ideal for FencePost Problem
'''
numnberStep = (end // step) + 1
linespaceResult = np.linspace(start,end ,numnberStep)
print(linespaceResult)

'''
OUTPUT:
[0 3 6 9]
[ 0.  3.  6.  9. 12.]
'''