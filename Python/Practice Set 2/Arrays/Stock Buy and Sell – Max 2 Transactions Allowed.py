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


def memoized():
    """
        Time complexity is O(n) and space complexity is O(n + n).
    """
    def get_max_profit(arr):
        n = len(arr)
        dp = {i: {j: {k: None for k in range(3)} for j in [True, False]} for i in range(n + 1)}
        return solve(arr, 0, True, 2, n, dp)

    def solve(arr, i, j, k, n, dp):
        if i == n:
            return 0
        if k == 0:
            return 0
        if dp[i][j][k] is not None:
            return dp[i][j][k]
        if j:
            dp[i][j][k] = max(
                -arr[i] + solve(arr, i + 1, not j, k, n, dp),
                solve(arr, i + 1, j, k, n, dp)
            )
        else:
            dp[i][j][k] = max(
                arr[i] + solve(arr, i + 1, not j, k - 1, n, dp),
                solve(arr, i + 1, j, k, n, dp)
            )
        return dp[i][j][k]

    print(get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(get_max_profit([1, 3, 1, 2, 4, 8]))
    print(get_max_profit([5, 4, 3, 2, 1]))
    print(get_max_profit([8, 5, 1, 3, 10]))
    print(get_max_profit([2, 6, 5, 2]))
    print(get_max_profit([1, 2, 3, 5]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def get_max_profit(arr):
        n = len(arr)
        dp = {i: {j: {k: 0 for k in range(3)} for j in [True, False]} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for j in [True, False]:
                for k in range(1, 3):
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
        return dp[0][True][2]

    print(get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(get_max_profit([1, 3, 1, 2, 4, 8]))
    print(get_max_profit([5, 4, 3, 2, 1]))
    print(get_max_profit([8, 5, 1, 3, 10]))
    print(get_max_profit([2, 6, 5, 2]))
    print(get_max_profit([1, 2, 3, 5]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def get_max_profit(arr):
        n = len(arr)
        nxt = {j: {k: 0 for k in range(3)} for j in [True, False]}
        for i in range(n - 1, -1, -1):
            curr = {j: {k: 0 for k in range(3)} for j in [True, False]}
            for j in [True, False]:
                for k in range(1, 3):
                    if j:
                        curr[j][k] = max(
                            -arr[i] + nxt[not j][k],
                            nxt[j][k]
                        )
                    else:
                        curr[j][k] = max(
                            arr[i] + nxt[not j][k - 1],
                            nxt[j][k]
                        )
            nxt = curr
        return nxt[True][2]

    print(get_max_profit([3, 3, 5, 0, 0, 3, 1, 4]))
    print(get_max_profit([1, 3, 1, 2, 4, 8]))
    print(get_max_profit([5, 4, 3, 2, 1]))
    print(get_max_profit([8, 5, 1, 3, 10]))
    print(get_max_profit([2, 6, 5, 2]))
    print(get_max_profit([1, 2, 3, 5]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
