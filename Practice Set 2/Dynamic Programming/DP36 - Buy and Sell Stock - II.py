# Problem link - https://www.geeksforgeeks.org/stock-buy-sell/
# Solution - https://www.youtube.com/watch?v=nGJmxkUJQGs&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=37


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, can_buy, n):
        if i == n:
            return 0

        if can_buy:
            return max(
                -arr[i] + solve(arr, i + 1, False, n),
                solve(arr, i + 1, True, n)
            )
        else:
            return max(
                arr[i] + solve(arr, i + 1, True, n),
                solve(arr, i + 1, False, n)
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
        Time complexity is O(2n) and space complexity is O(3n).
    """
    def solve(arr, i, can_buy, n, dp):
        if i == n:
            return 0

        if dp[i][can_buy] is not None:
            return dp[i][can_buy]

        if can_buy:
            dp[i][can_buy] = max(
                -arr[i] + solve(arr, i + 1, False, n, dp),
                solve(arr, i + 1, True, n, dp)
            )
        else:
            dp[i][can_buy] = max(
                arr[i] + solve(arr, i + 1, True, n, dp),
                solve(arr, i + 1, False, n, dp)
            )
        return dp[i][can_buy]

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


def tabulation():
    """
        Time complexity is O(2n) and space complexity is O(2n).
    """
    def max_profit(arr):
        n = len(arr)
        dp = {i: {True: 0, False: 0} for i in range(n + 1)}
        for i in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[i][can_buy] = max(
                        -arr[i] + dp[i + 1][False],
                        dp[i + 1][True]
                    )
                else:
                    dp[i][can_buy] = max(
                        arr[i] + dp[i + 1][True],
                        dp[i + 1][False]
                    )
        return dp[0][True]

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([1, 2, 3, 4, 5, 6, 7]))
    print(max_profit([7, 6, 5, 4, 3, 2, 1]))
    print(max_profit([1, 2, 3, 4, 5]))
    print(max_profit([100, 180, 260, 310, 40, 535, 695]))
    print(max_profit([4, 2, 2, 2, 4]))


def space_optimized():
    """
        Time complexity is O(2n) and space complexity is O(1).
    """
    def max_profit(arr):
        n = len(arr)
        nxt = {True: 0, False: 0}
        for i in range(n - 1, -1, -1):
            curr = {True: 0, False: 0}
            for can_buy in [True, False]:
                if can_buy:
                    curr[can_buy] = max(
                        -arr[i] + nxt[False],
                        nxt[True]
                    )
                else:
                    curr[can_buy] = max(
                        arr[i] + nxt[True],
                        nxt[False]
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
