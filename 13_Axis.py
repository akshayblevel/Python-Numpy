import numpy as np

# define a numpy array
twodarr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape: ",twodarr.shape) # Shape:  (2, 3) — 2 rows, 3 columns

print("Mean: ", np.mean(twodarr, axis=1)) # Mean:  [2. 5.]
'''
axis=1 means: compute mean across columns (i.e., row-wise).
So:
Row 1: mean of [1, 2, 3] → (1+2+3)/3 = 2.0
Row 2: mean of [4, 5, 6] → (4+5+6)/3 = 5.0
'''

print("Mean: ", np.mean(twodarr, axis=0)) # Mean:  [2.5 3.5 4.5]
'''
axis=0 means: compute mean down the rows (i.e., column-wise).
So:
Col 1: mean of [1, 4] → (1+4)/2 = 2.5
Col 2: mean of [2, 5] → (2+5)/2 = 3.5
Col 3: mean of [3, 6] → (3+6)/2 = 4.5
'''

threedarr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

print("Mean: ", np.mean(threedarr, axis=1))
'''
Compute the mean across rows within each block (i.e., between [1,2,3] and [4,5,6], then [7,8,9] and [10,11,12]).
Shape becomes (2, 3) (since axis 1 is removed).
[
  [(1+4)/2, (2+5)/2, (3+6)/2],     → [2.5, 3.5, 4.5]
  [(7+10)/2, (8+11)/2, (9+12)/2]   → [8.5, 9.5, 10.5]
]

OUTPUT:
Mean:  [[ 2.5  3.5  4.5]
 [ 8.5  9.5 10.5]]
'''

print("Mean: ", np.mean(threedarr, axis=0))
'''
Compute mean between blocks — i.e., threedarr[0] vs. threedarr[1].
Shape becomes (2, 3) (axis 0 is removed).
[
  [(1+7)/2, (2+8)/2, (3+9)/2],      → [4.0, 5.0, 6.0]
  [(4+10)/2, (5+11)/2, (6+12)/2]    → [7.0, 8.0, 9.0]
]

OUTPUT:
Mean:  [[4. 5. 6.]
 [7. 8. 9.]]
'''

print("Mean: ", np.mean(threedarr, axis=2))
'''
Compute mean across columns within each row (axis=2).
Shape becomes (2, 2) — the innermost dimension is reduced.
For [1, 2, 3]: (1+2+3)/3 = 2.0
For [4, 5, 6]: (4+5+6)/3 = 5.0
For [7, 8, 9]: (7+8+9)/3 = 8.0
For [10, 11, 12]: (10+11+12)/3 = 11.0

OUTPUT:
Mean:  [[ 2.  5.]
 [ 8. 11.]]
'''