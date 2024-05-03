import numpy as np
def find_k_largest_indices(arr, k):
    # Checking if k is greater than the number of elements in the array
    if k > len(arr):
        raise ValueError("k cannot be greater than the number of elements in the array")

    # get the indices that would sort the array
    indices_sorted = np.argsort(arr)

    # last k indices of the sorted indices array, which correspond to the k largest elements
    k_largest_indices = indices_sorted[-k:]

    # reverse the result to get the largest first
    return k_largest_indices[::-1]


arr = np.array([10, 65, 22, 75, 34, 89, 54])
k = 3
largest_indices = find_k_largest_indices(arr, k)
print(f"Indices of the {k} largest values are: {largest_indices}")
