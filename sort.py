def pivot_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage:
# sorted_list = pivot_sort([3, 6, 8, 10, 1, 2, 1])
# print(sorted_list)  # Output: [1, 1, 2, 3, 6, 8, 10]