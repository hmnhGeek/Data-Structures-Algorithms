# Problem link - https://www.geeksforgeeks.org/stock-buy-sell/
# Solution - https://www.youtube.com/watch?v=nGJmxkUJQGs&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=37


def recursive():
    def max_profit(arr):
        """
            Time complexity is exponential and space complexity is O(n).
        """
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
                arr[i] + solve(arr, i + 1, not j, n),
                solve(arr, i + 1, j, n)
            )

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


def memoized():
    def max_profit(arr):
        """
            Time complexity is O(n) and space complexity is O(2n).
        """
        n = len(arr)
        dp = {i: {True: None, False: None} for i in range(n + 1)}
        return solve(arr, 0, True, n, dp)

    def solve(arr, i, j, n, dp):
        if i >= n:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if j:
            dp[i][j] = max(
                -arr[i] + solve(arr, i + 1, not j, n, dp),
                solve(arr, i + 1, j, n, dp)
            )
        else:
            dp[i][j] = max(
                arr[i] + solve(arr, i + 1, not j, n, dp),
                solve(arr, i + 1, j, n, dp)
            )
        return dp[i][j]

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


def tabulation():
    def max_profit(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        n = len(arr)
        dp = {i: {True: 0, False: 0} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for j in [True, False]:
                if j:
                    dp[i][j] = max(
                        -arr[i] + dp[i + 1][not j],
                        dp[i + 1][j]
                    )
                else:
                    dp[i][j] = max(
                        arr[i] + dp[i + 1][not j],
                        dp[i + 1][j]
                    )
        return dp[0][True]

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


def space_optimized():
    def max_profit(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        n = len(arr)
        nxt = {True: 0, False: 0}
        for i in range(n - 1, -1, -1):
            curr = {True: 0, False: 0}
            for j in [True, False]:
                if j:
                    curr[j] = max(
                        -arr[i] + nxt[not j],
                        nxt[j]
                    )
                else:
                    curr[j] = max(
                        arr[i] + nxt[not j],
                        nxt[j]
                    )
            nxt = curr
        return nxt[True]

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
