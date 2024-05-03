import numpy as np
bidimensional = np.array([[10, 2, 30],
                          [7, 50, 6],
                          [40, 80, 9]])
sorted_indices = np.argsort(bidimensional[:, 0])
sorted_array = bidimensional[sorted_indices]
print("Original Array:")
print(bidimensional)
print("Sorted Array by the First Column:")
print(sorted_array)