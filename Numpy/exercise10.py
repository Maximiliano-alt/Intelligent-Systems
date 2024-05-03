import numpy as np
bidimensional = np.arange(12).reshape(4,3)
#mean of each row
mean = np.mean(bidimensional,axis=1,keepdims=True)
#standard deviation of each row
std_deviation = np.std(bidimensional,axis=1,keepdims=True)
normalized_bidimensional = (bidimensional - mean) / std_deviation
print("Numpy bidimensional Array: \n",bidimensional)
print("Normalized bidimensional Array: \n",normalized_bidimensional)