def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, index, can_buy, n):
        if index >= n:
            return 0
        if can_buy:
            return max(
                -arr[index] + solve(arr, index + 1, False, n),
                solve(arr, index + 1, True, n)
            )
        else:
            return max(
                arr[index] + solve(arr, index + 1, True, n),
                solve(arr, index + 1, False, n)
            )

    def max_profit(arr):
        n = len(arr)
        return solve(arr, 0, True, n)

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(n + n).
    """
    def solve(arr, index, can_buy, n, dp):
        if index >= n:
            return 0
        if dp[index][can_buy] is not None:
            return dp[index][can_buy]
        if can_buy:
            dp[index][can_buy] = max(
                -arr[index] + solve(arr, index + 1, False, n, dp),
                solve(arr, index + 1, True, n, dp)
            )
        else:
            dp[index][can_buy] = max(
                arr[index] + solve(arr, index + 1, True, n, dp),
                solve(arr, index + 1, False, n, dp)
            )
        return dp[index][can_buy]

    def max_profit(arr):
        n = len(arr)
        dp = {i: {True: None, False: None} for i in range(n + 1)}
        return solve(arr, 0, True, n, dp)

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


recursive()
print()
memoized()
