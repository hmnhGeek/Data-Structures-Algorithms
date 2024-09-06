def solve(arr, index, length, max_val):
    if index == 0:
        if arr[0] < max_val:
            return length + 1
        return length

    left = float('-inf')
    if arr[index] < max_val:
        left = solve(arr, index - 1, length + 1, arr[index])

    right = solve(arr, index - 1, length, max_val)
    return max(left, right)


def get_length_of_longest_increasing_subsequence(arr):
    n = len(arr)
    return max(
        solve(arr, n - 1, 0, float('inf')),
        solve(arr, n - 1, 0, float('inf'))
    )


print(get_length_of_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(get_length_of_longest_increasing_subsequence([5, 4, 11, 1, 16, 8]))
print(get_length_of_longest_increasing_subsequence([1, 2, 2]))