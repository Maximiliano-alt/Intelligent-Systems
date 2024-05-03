import numpy as np
np.random.seed(0)

# 7x5 array with numbers drawn from a normal distribution
array = np.random.randn(7, 5)

print("Original Array:")
print(array)

# Set all negative elements to zero
array[array < 0] = 0

print("Modified Array (Negative elements set to zero):")
print(array)
