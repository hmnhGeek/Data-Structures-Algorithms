def max_subarray_sum(arr):
    max_sum = -1e6
    curr = 0
    for i in range(len(arr)):
        curr += arr[i]
        max_sum = max(max_sum, curr)
        if curr < 0:
            curr = 0
    return max_sum


print(max_subarray_sum([2, 3, -8, 7, -1, 2, 3]))
print(max_subarray_sum([-2, -4]))
print(max_subarray_sum([5, 4, 1, 7, 8]))
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_sum([4, -1, 2, -7, 3, 4]))
