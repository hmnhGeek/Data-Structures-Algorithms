def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def min_swaps_for_k_together(arr, k):
    i, j, n = 0, len(arr) - 1, len(arr)
    swap_count = 0
    while i < j:
        while i < n and arr[i] < k:
            i += 1
        while j >= 0 and arr[j] > k:
            j -= 1
        if i < j:
            swap(arr, i, j)
            swap_count += 1
            i += 1
            j -= 1

    return swap_count


print(min_swaps_for_k_together([2, 1, 5, 6, 3], 3))
print(min_swaps_for_k_together([2, 7, 9, 5, 8, 7, 4], 6))
print(min_swaps_for_k_together([5, 4, 6, 10, 35, 30, 8], 9))
print(min_swaps_for_k_together([1, 15, 18, 3, 14, 18, 5], 9))
print(min_swaps_for_k_together([1, 12, 10, 3, 14, 10, 5], 8))
print(min_swaps_for_k_together([1, 1, 2, 3, 1], 1))