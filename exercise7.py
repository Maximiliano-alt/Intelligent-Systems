import numpy as np
unidimensional = np.arange(9)

elements = len(unidimensional)
perfect_sqrt = int(np.sqrt(elements))#  checks perfect sqrt
if perfect_sqrt * perfect_sqrt != elements:
    print("It is not possible to rearrange the array into a square matrix.")
else:
    square_matrix = unidimensional.reshape(perfect_sqrt, perfect_sqrt)
    print("square matrix:")
    print(square_matrix)


