import numpy as np
# array with random numbers from a uniform distribution between 0 and 1
array = np.random.rand(6, 7)
# first two columns to zero
array[:, 0:2] = 0
# last three columns to one
array[:, -3:] = 1
print("Modified Array:")
print(array)
