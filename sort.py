def pivot_sort(arr):
    """
    Sort an array in ascending order using pivot sort (quicksort).
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return pivot_sort(left) + middle + pivot_sort(right)