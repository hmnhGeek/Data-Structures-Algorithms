def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def get_max_profit(arr):
        n = len(arr)
        return solve(arr, 0, True, 2, n)

    def solve(arr, i, j, k, n):
        if i == n:
            return 0
        if k == 0:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, k, n),
                solve(arr, i + 1, j, k, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, not j, k - 1, n),
                solve(arr, i + 1, j, k, n)
            )

    print(get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(get_max_profit([1, 3, 1, 2, 4, 8]))
    print(get_max_profit([5, 4, 3, 2, 1]))
    print(get_max_profit([8, 5, 1, 3, 10]))
    print(get_max_profit([2, 6, 5, 2]))
    print(get_max_profit([1, 2, 3, 5]))


recursive()
print()