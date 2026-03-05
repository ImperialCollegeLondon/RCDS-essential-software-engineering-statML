import numpy as np

def pivot_sort(arr):
    """
    Hi Lucy this is my new docstring (lucy was here)

    Args:
        arr: Numpy array of comparable elements
        
    Returns:
        Sorted numpy array in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = arr[arr < pivot]
    middle = arr[arr == pivot]
    right = arr[arr > pivot]
    
    return np.concatenate([pivot_sort(left), middle, pivot_sort(right)])