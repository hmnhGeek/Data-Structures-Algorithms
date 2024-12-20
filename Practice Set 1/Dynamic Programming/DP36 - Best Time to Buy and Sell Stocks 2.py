# Problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Solution - https://www.youtube.com/watch?v=nGJmxkUJQGs&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=37


def recursive():
    """
        Time complexity is exponential and space complexity is O(n)
    """

    def solve(prices, index, can_buy, n):
        if index == n:
            return 0

        if can_buy:
            return max(
                -prices[index] + solve(prices, index + 1, False, n),
                solve(prices, index + 1, True, n)
            )
        else:
            return max(
                prices[index] + solve(prices, index + 1, True, n),
                solve(prices, index + 1, False, n)
            )

    def best_time(prices):
        n = len(prices)
        return solve(prices, 0, True, n)

    print(best_time([7, 1, 5, 3, 6, 4]))
    print(best_time([1, 2, 3, 4, 5, 6, 7]))
    print(best_time([7, 6, 5, 4, 3, 2, 1]))
    print(best_time([1, 2, 3, 4, 5]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(n + n)
    """

    def solve(prices, index, can_buy, n, dp):
        if index == n:
            return 0

        if dp[index][can_buy] is not None:
            return dp[index][can_buy]

        if can_buy:
            dp[index][can_buy] = max(
                -prices[index] + solve(prices, index + 1, False, n, dp),
                solve(prices, index + 1, True, n, dp)
            )
        else:
            dp[index][can_buy] = max(
                prices[index] + solve(prices, index + 1, True, n, dp),
                solve(prices, index + 1, False, n, dp)
            )
        return dp[index][can_buy]

    def best_time(prices):
        n = len(prices)
        dp = {i: {True: None, False: None} for i in range(n)}
        return solve(prices, 0, True, n, dp)

    print(best_time([7, 1, 5, 3, 6, 4]))
    print(best_time([1, 2, 3, 4, 5, 6, 7]))
    print(best_time([7, 6, 5, 4, 3, 2, 1]))
    print(best_time([1, 2, 3, 4, 5]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n)
    """
    def best_time(prices):
        n = len(prices)
        dp = {i: {True: 0, False: 0} for i in range(n + 1)}

        for index in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[index][can_buy] = max(-prices[index] + dp[index + 1][False], dp[index + 1][True])
                else:
                    dp[index][can_buy] = max(prices[index] + dp[index + 1][True], dp[index + 1][False])
        return dp[0][True]

    print(best_time([7, 1, 5, 3, 6, 4]))
    print(best_time([1, 2, 3, 4, 5, 6, 7]))
    print(best_time([7, 6, 5, 4, 3, 2, 1]))
    print(best_time([1, 2, 3, 4, 5]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def best_time(prices):
        n = len(prices)
        nxt = {True: 0, False: 0}

        for index in range(n - 1, -1, -1):
            curr = {True: 0, False: 0}
            for can_buy in [True, False]:
                if can_buy:
                    curr[can_buy] = max(-prices[index] + nxt[False], nxt[True])
                else:
                    curr[can_buy] = max(prices[index] + nxt[True], nxt[False])
            nxt = curr
        return nxt[True]

    print(best_time([7, 1, 5, 3, 6, 4]))
    print(best_time([1, 2, 3, 4, 5, 6, 7]))
    print(best_time([7, 6, 5, 4, 3, 2, 1]))
    print(best_time([1, 2, 3, 4, 5]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
