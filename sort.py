def pivot_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return pivot_sort(left) + [pivot] + pivot_sort(right)


if __name__ == "__main__":
    # Demonstration of pivot_sort usage
    unsorted_list = [3, 6, 2, 7, 1, 4, 8]
    sorted_list = pivot_sort(unsorted_list)
    print("Unsorted:", unsorted_list)
    print("Sorted:", sorted_list)