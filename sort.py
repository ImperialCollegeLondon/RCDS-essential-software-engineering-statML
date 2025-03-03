def pivot_sort(lst):
    """
    Sorts a list of elements using the pivot sort algorithm (a variation of quicksort).
    Args:
        lst (list): The list of elements to be sorted.
    Returns:
        list: A new list containing the sorted elements.
    Example:
        >>> pivot_sort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
    """

    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less_than_pivot = [x for x in lst[1:] if x <= pivot]
        greater_than_pivot = [x for x in lst[1:] if x > pivot]
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage
if __name__ == "__main__":
    unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = pivot_sort(unsorted_list)
    print("Sorted list:", sorted_list)

