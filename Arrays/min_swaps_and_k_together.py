def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def min_swaps_for_k_together(arr, k):
    n = len(arr)
    required_window_size = 0
    for i in arr:
        if i <= k:
            required_window_size += 1

    greater_than_k_in_window = 0
    for i in range(required_window_size):
        if arr[i] > k:
            greater_than_k_in_window += 1

    for i in range(1, n - required_window_size + 1):
        local_greater_elements = greater_than_k_in_window
        start = i
        end = i + required_window_size - 1
        if arr[end] > k:
            local_greater_elements += 1
        if arr[start - 1] > k:
            local_greater_elements -= 1
        greater_than_k_in_window = min(greater_than_k_in_window, local_greater_elements)

    return greater_than_k_in_window


print(min_swaps_for_k_together([2, 1, 5, 6, 3], 3))
print(min_swaps_for_k_together([2, 7, 9, 5, 8, 7, 4], 6))
print(min_swaps_for_k_together([5, 4, 6, 10, 35, 30, 8], 9))
print(min_swaps_for_k_together([1, 15, 18, 3, 14, 18, 5], 9))
print(min_swaps_for_k_together([1, 12, 10, 3, 14, 10, 5], 8))
print(min_swaps_for_k_together([1, 1, 2, 3, 1], 1))
print(min_swaps_for_k_together([7, 3, 2, 5, 1, 6, 4], 4))