def get_val_at(arr, index, n):
    if index not in range(n):
        return 1e6
    return arr[index]


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, index, prev, n):
        if index == 0:
            return 1 if arr[0] < get_val_at(arr, prev, n) else 0
        left = -1e6
        if arr[index] < get_val_at(arr, prev, n):
            left = 1 + solve(arr, index - 1, index, n)
        right = solve(arr, index - 1, prev, n)
        return max(left, right)

    def get_lis_length(arr):
        n = len(arr)
        return solve(arr, n - 1, 1e6, n)

    print(get_lis_length([10, 9, 2, 5, 3, 7, 101, 18]))
    print(get_lis_length([5, 4, 11, 1, 16, 8]))
    print(get_lis_length([1, 2, 2]))
    print(get_lis_length([0, 1, 0, 3, 2, 3]))
    print(get_lis_length([7, 7, 7, 7, 7, 7, 7]))
    print(get_lis_length([3, 10, 2, 1, 20]))
    print(get_lis_length([30, 20, 10]))
    print(get_lis_length([10, 20, 35, 80]))


recursive()