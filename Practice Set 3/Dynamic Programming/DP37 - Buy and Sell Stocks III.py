def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, index, can_buy, transactions, k, n):
        if transactions == k:
            return 0
        if index >= n:
            return 0
        if can_buy:
            return max(
                -arr[index] + solve(arr, index + 1, False, transactions, k, n),
                solve(arr, index + 1, True, transactions, k, n)
            )
        else:
            return max(
                arr[index] + solve(arr, index + 1, True, transactions + 1, k, n),
                solve(arr, index + 1, False, transactions, k, n)
            )

    def buy_sell(arr, k):
        n = len(arr)
        return solve(arr, 0, True, 0, k, n)

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(buy_sell([1, 3, 1, 2, 4, 8], 2))
    print(buy_sell([5, 4, 3, 2, 1], 2))
    print(buy_sell([1, 2, 3, 4, 5], 2))
    print(buy_sell([7, 1, 5, 3, 6, 4], 2))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """
    def solve(arr, index, can_buy, transactions, k, n, dp):
        if transactions == k:
            return 0
        if index >= n:
            return 0
        if dp[index][can_buy][transactions] is not None:
            return dp[index][can_buy][transactions]
        if can_buy:
            dp[index][can_buy][transactions] = max(
                -arr[index] + solve(arr, index + 1, False, transactions, k, n, dp),
                solve(arr, index + 1, True, transactions, k, n, dp)
            )
        else:
            dp[index][can_buy][transactions] = max(
                arr[index] + solve(arr, index + 1, True, transactions + 1, k, n, dp),
                solve(arr, index + 1, False, transactions, k, n, dp)
            )
        return dp[index][can_buy][transactions]

    def buy_sell(arr, k):
        n = len(arr)
        dp = {i: {True: {j: None for j in range(k + 1)}, False: {j: None for j in range(k + 1)}} for i in range(n + 1)}
        return solve(arr, 0, True, 0, k, n, dp)

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(buy_sell([1, 3, 1, 2, 4, 8], 2))
    print(buy_sell([5, 4, 3, 2, 1], 2))
    print(buy_sell([1, 2, 3, 4, 5], 2))
    print(buy_sell([7, 1, 5, 3, 6, 4], 2))


recursive()
print()
memoized()
