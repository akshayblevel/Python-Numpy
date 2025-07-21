from math import isnan
import numpy as np

intArray = np.array([14, 10, 81, 17, 10])

print("Sum:", np.sum(intArray)) # Sum: 132
print("Mean:", np.mean(intArray)) # Mean: 26.4
print("Max:", np.max(intArray)) # Max: 81
print("Min:", np.min(intArray)) # Min: 10
print("Percentile",np.percentile(intArray,4)) # Percentile 10.0

intArray = np.array([14, 10, np.nan, 17, 10])
print("Sum:", np.nansum(intArray)) # Sum: 51.0
print("Mean:", np.nanmean(intArray)) # Mean: 12.75
print("Max:", np.nanmax(intArray)) # Max: 17.0
print("Min:", np.nanmin(intArray)) # Min: 10.0

print(np.isnan(intArray)) # [False False  True False False]

mask = ~np.isnan(intArray)  
print(intArray[mask])  # [14. 10. 17. 10.]