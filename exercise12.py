import numpy as np

bidimensional = np.arange(9).reshape(3,3)

# Find the index of the minimum element
min_index = np.unravel_index(np.argmin(bidimensional), bidimensional.shape)
# Find the index of the maximum element
max_index = np.unravel_index(np.argmax(bidimensional), bidimensional.shape)
print("Minimum index element: ",min_index," \n")
print("Maximum index element: ",max_index," \n")


