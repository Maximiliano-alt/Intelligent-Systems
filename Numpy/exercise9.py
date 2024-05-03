import numpy as np
unidimensional = np.array([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5])#unidimensional array
# finding unique values and occurrences of numpy array
unique_values, occurrences = np.unique(unidimensional, return_counts=True)
# dictionary to show the unique values and their occurences
occurrences_dict = dict(zip(unique_values, occurrences))
print("Number of occurrences of each unique value: ",occurrences_dict)
