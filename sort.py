def pivot_sort(arr):
    """
    Sorts an array using the quicksort algorithm with the first element as the pivot.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.

    Example:
        >>> pivot_sort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage
if __name__ == "__main__":
    sample_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = pivot_sort(sample_list)
    print("Sorted list:", sorted_list)