# Problem link - https://www.naukri.com/code360/problems/highway-billboards_3125969
# Solution - https://www.youtube.com/watch?v=IGIe46xw3YY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=40


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


def memoized():
    """
        Time complexity is O(n) and space complexity is O(n + n).
    """
    def buy_sell(arr):
        n = len(arr)
        dp = {i: {j: None for j in [True, False]} for i in range(n + 2)}
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
                arr[i] + solve(arr, i + 2, not j, n, dp),
                solve(arr, i + 1, j, n, dp)
            )
        return dp[i][j]

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def buy_sell(arr):
        n = len(arr)
        dp = {i: {j: 0 for j in [True, False]} for i in range(n + 2)}
        for i in range(n - 1, -1, -1):
            for j in [True, False]:
                if j:
                    dp[i][j] = max(
                        -arr[i] + dp[i + 1][not j],
                        dp[i + 1][j]
                    )
                else:
                    dp[i][j] = max(
                        arr[i] + dp[i + 2][not j],
                        dp[i + 1][j]
                    )
        return dp[0][True]

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def buy_sell(arr):
        n = len(arr)
        nxt = {j: 0 for j in [True, False]}
        nxt2 = {j: 0 for j in [True, False]}
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
                        arr[i] + nxt2[not j],
                        nxt[j]
                    )
            nxt2 = nxt
            nxt = curr
        return nxt[True]

    print(buy_sell([4, 9, 0, 4, 10]))
    print(buy_sell([1, 2, 3, 4]))
    print(buy_sell([5, 4, 3]))
    print(buy_sell([1, 2, 3, 0, 2]))
    print(buy_sell([1]))
    print(buy_sell([3, 1, 6, 1, 2, 4]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
