import numpy as np
bidimensional = np.arange(9).reshape(3,3)
mean_elements = np.mean(bidimensional,axis=0)
print("Numpy Bidimensional Array: \n",bidimensional)
print("Mean of elements of each column: \n", mean_elements)