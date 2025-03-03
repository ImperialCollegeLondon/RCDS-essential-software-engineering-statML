def pivot_sort(arr):
    """
    Sorts an array using the pivot sort (a variation of quicksort) algorithm.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new list with the elements from arr sorted in ascending order.
    """
    if len(arr) < 2:  # Base case: if the array has 0 or 1 elements, it is already sorted
        return arr
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        # Elements less than or equal to the pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        # Elements greater than the pivot
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Recursively sort the sublists and concatenate them with the pivot
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage:
# sorted_list = pivot_sort([3, 6, 8, 10, 1, 2, 1])
# print(sorted_list)  # Output: [1, 1, 2, 3, 6, 8, 10]