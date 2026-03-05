import numpy as np

def pivot_sort(arr):
    """
    Sorts a list in ascending order using the quicksort algorithm.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = arr[arr < pivot]
    middle = arr[arr == pivot]
    right = arr[arr > pivot]
    
    return np.concatenate([pivot_sort(left), middle, pivot_sort(right)])