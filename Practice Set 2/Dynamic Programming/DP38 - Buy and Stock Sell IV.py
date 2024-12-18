def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, can_buy, tx, k, n):
        if tx == k:
            return 0
        if i == n:
            return 0
        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, tx, k, n),
                solve(arr, i + 1, True, tx, k, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, True, tx + 1, k, n),
                solve(arr, i + 1, False, tx, k, n)
            )

    def buy_and_sell(arr, k):
        n = len(arr)
        return solve(arr, 0, True, 0, k, n)

    print(buy_and_sell([3, 2, 6, 5, 0, 3], 2))
    print(buy_and_sell([8, 5, 1, 3, 10], 2))
    print(buy_and_sell([10, 8, 6, 2], 2))
    print(buy_and_sell([2, 6, 5, 2], 0))
    print(buy_and_sell([1, 2, 3, 5], 2))
    print(buy_and_sell([2, 4, 1], 2))
    print(buy_and_sell([10, 22, 5, 75, 65, 80], 2))
    print(buy_and_sell([12, 14, 17, 10, 14, 13, 12, 15], 3))
    print(buy_and_sell([100, 30, 15, 10, 8, 25, 80], 3))
    print(buy_and_sell([90, 80, 70, 60, 50], 1))


def memoized():
    """
        Time complexity is O(2nk) and space complexity is O(n + 2nk).
    """
    def solve(arr, i, can_buy, tx, k, n, dp):
        if tx == k:
            return 0
        if i == n:
            return 0
        if dp[i][can_buy][tx] is not None:
            return dp[i][can_buy][tx]
        if can_buy:
            dp[i][can_buy][tx] = max(
                -arr[i] + solve(arr, i + 1, False, tx, k, n, dp),
                solve(arr, i + 1, True, tx, k, n, dp)
            )
        else:
            dp[i][can_buy][tx] = max(
                arr[i] + solve(arr, i + 1, True, tx + 1, k, n, dp),
                solve(arr, i + 1, False, tx, k, n, dp)
            )
        return dp[i][can_buy][tx]

    def buy_and_sell(arr, k):
        n = len(arr)
        dp = {i: {True: {j: None for j in range(k + 1)}, False: {j: None for j in range(k + 1)}} for i in range(n + 1)}
        return solve(arr, 0, True, 0, k, n, dp)

    print(buy_and_sell([3, 2, 6, 5, 0, 3], 2))
    print(buy_and_sell([8, 5, 1, 3, 10], 2))
    print(buy_and_sell([10, 8, 6, 2], 2))
    print(buy_and_sell([2, 6, 5, 2], 0))
    print(buy_and_sell([1, 2, 3, 5], 2))
    print(buy_and_sell([2, 4, 1], 2))
    print(buy_and_sell([10, 22, 5, 75, 65, 80], 2))
    print(buy_and_sell([12, 14, 17, 10, 14, 13, 12, 15], 3))
    print(buy_and_sell([100, 30, 15, 10, 8, 25, 80], 3))
    print(buy_and_sell([90, 80, 70, 60, 50], 1))


def tabulation():
    """
        Time complexity is O(2nk) and space complexity is O(2nk).
    """
    def buy_and_sell(arr, k):
        n = len(arr)
        dp = {i: {True: {j: 0 for j in range(k + 1)}, False: {j: 0 for j in range(k + 1)}} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                for tx in range(k - 1, -1, -1):
                    if can_buy:
                        dp[i][can_buy][tx] = max(
                            -arr[i] + dp[i + 1][False][tx],
                            dp[i + 1][True][tx]
                        )
                    else:
                        dp[i][can_buy][tx] = max(
                            arr[i] + dp[i + 1][True][tx + 1],
                            dp[i + 1][False][tx]
                        )
        return dp[0][True][0]

    print(buy_and_sell([3, 2, 6, 5, 0, 3], 2))
    print(buy_and_sell([8, 5, 1, 3, 10], 2))
    print(buy_and_sell([10, 8, 6, 2], 2))
    print(buy_and_sell([2, 6, 5, 2], 0))
    print(buy_and_sell([1, 2, 3, 5], 2))
    print(buy_and_sell([2, 4, 1], 2))
    print(buy_and_sell([10, 22, 5, 75, 65, 80], 2))
    print(buy_and_sell([12, 14, 17, 10, 14, 13, 12, 15], 3))
    print(buy_and_sell([100, 30, 15, 10, 8, 25, 80], 3))
    print(buy_and_sell([90, 80, 70, 60, 50], 1))


recursive()
print()
memoized()
print()
tabulation()