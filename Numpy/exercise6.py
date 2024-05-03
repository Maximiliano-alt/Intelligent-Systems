import numpy as np
unidimensionalArray = np.arange(12)#any length
print("Numpy unidimensional Array: \n",unidimensionalArray)
aux = 0
if len(unidimensionalArray) < 12:# if the array is shorter than 12 elements, add zeros to complete 12 elements
    aux = 12 - len(unidimensionalArray)
    unidimensionalArray = np.concatenate([unidimensionalArray,np.zeros((aux,), dtype=int)])
elif len(unidimensionalArray) > 12:#otherwise the array only takes 12 elements
    aux = len(unidimensionalArray) - 12
    unidimensionalArray = np.delete(unidimensionalArray,np.s_[-aux:])#deletes the rest

if isinstance(unidimensionalArray, list):# if the array is a list, it converts to a numpy array
    unidimensionalArray = np.array(unidimensionalArray)
print("Numpy bidimensional Array: \n",unidimensionalArray.reshape(4, 3))#reshapes the array into a bidimensional array