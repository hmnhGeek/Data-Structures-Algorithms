def recursive():
    def buy_and_sell(arr, transaction_fee):
        n = len(arr)
        return solve(arr, 0, True, transaction_fee, n)

    def solve(arr, i, j, k, n):
        if i >= n:
            return 0
        if j:
            return max(
                -arr[i] + solve(arr, i + 1, not j, k, n),
                solve(arr, i + 1, j, k, n)
            )
        else:
            return max(
                arr[i] - k + solve(arr, i + 1, not j, k, n),
                solve(arr, i + 1, j, k, n)
            )

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


def memoized():
    def buy_and_sell(arr, transaction_fee):
        """
            Time complexity is O(n) and space complexity is O(n + n).
        """
        n = len(arr)
        dp = {i: {j: None for j in [True, False]} for i in range(n)}
        return solve(arr, 0, True, transaction_fee, n, dp)

    def solve(arr, i, j, k, n, dp):
        if i >= n:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if j:
            dp[i][j] = max(
                -arr[i] + solve(arr, i + 1, not j, k, n, dp),
                solve(arr, i + 1, j, k, n, dp)
            )
        else:
            dp[i][j] = max(
                arr[i] - k + solve(arr, i + 1, not j, k, n, dp),
                solve(arr, i + 1, j, k, n, dp)
            )
        return dp[i][j]

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


def tabulation():
    def buy_and_sell(arr, transaction_fee):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        n = len(arr)
        dp = {i: {j: 0 for j in [True, False]} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for j in [True, False]:
                if j:
                    dp[i][j] = max(
                        -arr[i] + dp[i + 1][not j],
                        dp[i + 1][j]
                    )
                else:
                    dp[i][j] = max(
                        arr[i] - transaction_fee + dp[i + 1][not j],
                        dp[i + 1][j]
                    )
        return dp[0][True]

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


def space_optimized():
    def buy_and_sell(arr, transaction_fee):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        n = len(arr)
        nxt = {j: 0 for j in [True, False]}
        for i in range(n - 1, -1, -1):
            curr = {j: 0 for j in [True, False]}
            for j in [True, False]:
                if j:
                    curr[j] = max(
                        -arr[i] + nxt[not j],
                        nxt[j]
                    )
                else:
                    curr[j] = max(
                        arr[i] - transaction_fee + nxt[not j],
                        nxt[j]
                    )
            nxt = curr
        return nxt[True]

    print(buy_and_sell([1, 3, 2, 8, 4, 9], 2))
    print(buy_and_sell([1, 2, 3], 1))
    print(buy_and_sell([1, 3, 5, 6], 2))
    print(buy_and_sell([1, 3, 7, 5, 10, 3], 3))
    print(buy_and_sell([6, 1, 7, 2, 8, 4], 2))
    print(buy_and_sell([7, 1, 5, 3, 6, 4], 1))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
