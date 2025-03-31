# Problem link - https://www.naukri.com/code360/problems/highway-billboards_3125969?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IGIe46xw3YY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=40


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(prices, index, can_buy, n):
        if index >= n:
            return 0

        if can_buy:
            return max(
                -prices[index] + solve(prices, index + 1, False, n),
                solve(prices, index + 1, True, n)
            )
        else:
            return max(
                prices[index] + solve(prices, index + 2, True, n),
                solve(prices, index + 1, False, n)
            )

    def best_time(prices):
        n = len(prices)
        return solve(prices, 0, True, n)

    print(best_time([4, 9, 0, 4, 10]))
    print(best_time([1, 2, 3, 4]))
    print(best_time([5, 4, 3]))


def memoized():
    """
        Time complexity is O(n) and space complexity is O(2n).
    """

    def solve(prices, index, can_buy, n, dp):
        if index >= n:
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
                prices[index] + solve(prices, index + 2, True, n, dp),
                solve(prices, index + 1, False, n, dp)
            )
        return dp[index][can_buy]

    def best_time(prices):
        n = len(prices)
        dp = {i: {j: None for j in [True, False]} for i in range(n)}
        return solve(prices, 0, True, n, dp)

    print(best_time([4, 9, 0, 4, 10]))
    print(best_time([1, 2, 3, 4]))
    print(best_time([5, 4, 3]))


def tabulation():
    """
        Time complexity is O(n) and space complexity is O(n).
    """
    def best_time(prices):
        n = len(prices)
        dp = {i: {j: 0 for j in [True, False]} for i in range(n + 2)}
        for index in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[index][can_buy] = max(-prices[index] + dp[index + 1][False], dp[index + 1][True])
                else:
                    dp[index][can_buy] = max(prices[index] + dp[index + 2][True], dp[index + 1][False])
        return dp[0][True]

    print(best_time([4, 9, 0, 4, 10]))
    print(best_time([1, 2, 3, 4]))
    print(best_time([5, 4, 3]))


def space_optimized():
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    def best_time(prices):
        n = len(prices)
        nxt2 = {j: 0 for j in [True, False]}
        nxt = {j: 0 for j in [True, False]}
        for index in range(n - 1, -1, -1):
            curr = {j: 0 for j in [True, False]}
            for can_buy in [True, False]:
                if can_buy:
                    curr[can_buy] = max(-prices[index] + nxt[False], nxt[True])
                else:
                    curr[can_buy] = max(prices[index] + nxt2[True], nxt[False])
            nxt2 = nxt
            nxt = curr
        return nxt[True]

    print(best_time([4, 9, 0, 4, 10]))
    print(best_time([1, 2, 3, 4]))
    print(best_time([5, 4, 3]))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()