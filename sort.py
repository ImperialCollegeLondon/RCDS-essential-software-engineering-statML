def pivot_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    
    # Partition the array into two sub-arrays:
    # 'left' with elements less than the pivot
    # 'right' with elements greater than or equal to the pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    
    # Recursively sort the sub-arrays and concatenate them with the pivot
    return pivot_sort(left) + [pivot] + pivot_sort(right)

def stalin_sort(arr):
    if not arr:
        return []
    
    result = [arr[0]]
    for num in arr[1:]:
        if num >= result[-1]:
            result.append(num)
    
    return result