import numpy as np
bidimensional = np.arange(9).reshape(3,3)
maximum = np.max(bidimensional,axis=1)
print("Numpy bidimensional Array: \n",bidimensional)#reshapes the array into a bidimensional array
print("Maximum of each row: ",maximum)