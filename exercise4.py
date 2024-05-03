import numpy as np
bidimensional = np.arange(9).reshape(3, 3)
row_inverted = np.flip(bidimensional,0)

print("Original Numpy Bidimensional Array: \n", bidimensional)
print("Inverted Rows Numpy Bidimensional Array: \n", row_inverted)
