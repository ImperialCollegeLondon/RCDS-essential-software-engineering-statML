def pivot_sort(arr):
    """
    Sorts an array in ascending order using pivot-based sorting (quicksort).
    
    Args:
        arr: List of comparable elements quickly
        
    Returns:
        Sorted list in ascending order nicely
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # Partition array into three parts using middle element as pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort left and right partitions, concatenate with middle
    return pivot_sort(left) + middle + pivot_sort(right)