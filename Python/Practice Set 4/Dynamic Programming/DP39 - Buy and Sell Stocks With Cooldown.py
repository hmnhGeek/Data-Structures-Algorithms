def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def buy_sell(arr):
        n = len(arr)
        return solve(arr, 0, True, n)

    def solve(arr, i, j, n):
        if i >= n:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, n),
                solve(arr, i + 1, j, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 2, not j, n),
                solve(arr, i + 1, j, n)
            )

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


recursive()
print()
