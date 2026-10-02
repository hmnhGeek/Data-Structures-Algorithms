def is_divisible(arr, i, j):
    if j is None:
        return True
    return arr[i] % j == 0 or j % arr[i] == 0


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def get_lds_length(arr):
        n = len(arr)
        return solve(arr, n - 1, None)

    def solve(arr, i, j):
        if i == 0:
            return 1 if is_divisible(arr, i, j) else 0
        if j is None:
            return max(1 + solve(arr, i - 1, arr[i]), solve(arr, i - 1, None))
        if is_divisible(arr, i, j):
            return max(1 + solve(arr, i - 1, arr[i]), solve(arr, i - 1, j))
        else:
            return solve(arr, i - 1, j)

    print(get_lds_length([1, 16, 7, 8, 4]))
    print(get_lds_length([1, 2, 5]))
    print(get_lds_length([3, 3, 3]))
    print(get_lds_length([1, 2, 4, 8]))
    print(get_lds_length([1, 2, 3]))
    print(get_lds_length([2, 4, 3, 8]))


recursive()
