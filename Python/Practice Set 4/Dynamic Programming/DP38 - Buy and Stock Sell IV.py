def recursive():
    def buy_sell(arr, k):
        n = len(arr)
        return solve(arr, 0, True, n, k)

    def solve(arr, i, j, n, k):
        if k == 0:
            return 0
        if i >= n:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, n, k),
                solve(arr, i + 1, j, n, k)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, not j, n, k - 1),
                solve(arr, i + 1, j, n, k)
            )

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(buy_sell([1, 3, 1, 2, 4, 8], 2))
    print(buy_sell([5, 4, 3, 2, 1], 2))
    print(buy_sell([1, 2, 3, 4, 5], 2))
    print(buy_sell([7, 1, 5, 3, 6, 4], 2))


def memoized():
    def buy_sell(arr, max_transactions_allowed):
        """
            Time complexity is O(n * k) and space complexity is O(n + nk).
        """
        n = len(arr)
        dp = {i: {j: {k: None for k in range(max_transactions_allowed + 1)} for j in [True, False]} for i in range(n + 1)}
        return solve(arr, 0, True, n, max_transactions_allowed, dp)

    def solve(arr, i, j, n, k, dp):
        if k == 0:
            return 0
        if i >= n:
            return 0
        if dp[i][j][k] is not None:
            return dp[i][j][k]
        if j:
            dp[i][j][k] = max(
                -arr[i] + solve(arr, i + 1, not j, n, k, dp),
                solve(arr, i + 1, j, n, k, dp)
            )
        else:
            dp[i][j][k] = max(
                arr[i] + solve(arr, i + 1, not j, n, k - 1, dp),
                solve(arr, i + 1, j, n, k, dp)
            )
        return dp[i][j][k]

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(buy_sell([1, 3, 1, 2, 4, 8], 2))
    print(buy_sell([5, 4, 3, 2, 1], 2))
    print(buy_sell([1, 2, 3, 4, 5], 2))
    print(buy_sell([7, 1, 5, 3, 6, 4], 2))


def tabulation():
    def buy_sell(arr, max_transactions_allowed):
        """
            Time complexity is O(n * k) and space complexity is O(nk).
        """
        n = len(arr)
        dp = {i: {j: {k: 0 for k in range(max_transactions_allowed + 1)} for j in [True, False]} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for j in [True, False]:
                for k in range(1, max_transactions_allowed + 1):
                    if j:
                        dp[i][j][k] = max(
                            -arr[i] + dp[i + 1][not j][k],
                            dp[i + 1][j][k]
                        )
                    else:
                        dp[i][j][k] = max(
                            arr[i] + dp[i + 1][not j][k - 1],
                            dp[i + 1][j][k]
                        )
        return dp[0][True][max_transactions_allowed]

    print(buy_sell([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(buy_sell([1, 3, 1, 2, 4, 8], 2))
    print(buy_sell([5, 4, 3, 2, 1], 2))
    print(buy_sell([1, 2, 3, 4, 5], 2))
    print(buy_sell([7, 1, 5, 3, 6, 4], 2))


recursive()
print()
memoized()
print()
tabulation()
print()
