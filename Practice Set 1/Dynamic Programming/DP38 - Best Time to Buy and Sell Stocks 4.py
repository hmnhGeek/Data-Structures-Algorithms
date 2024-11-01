# Problem link - https://www.naukri.com/code360/problems/best-time-to-buy-and-sell-stock_1080698?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IV1dHbk5CDc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=39


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(prices, index, can_buy, n, k):
        if k == 0:
            return 0

        if index == n:
            return 0

        if can_buy:
            return max(
                -prices[index] + solve(prices, index + 1, False, n, k),
                solve(prices, index + 1, True, n, k)
            )
        else:
            return max(
                prices[index] + solve(prices, index + 1, True, n, k - 1),
                solve(prices, index + 1, False, n, k)
            )

    def best_time(prices, num_transactions):
        n = len(prices)
        return solve(prices, 0, True, n, num_transactions)

    print(best_time([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(best_time([1, 3, 1, 2, 4, 8], 2))
    print(best_time([5, 4, 3, 2, 1], 2))
    print(best_time([8, 5, 1, 3, 10], 2))
    print(best_time([2, 6, 5, 2], 0))
    print(best_time([1, 2, 3, 5], 2))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + n*k).
    """
    def solve(prices, index, can_buy, n, k, dp):
        if k == 0:
            return 0

        if index == n:
            return 0

        if dp[index][can_buy][k] is not None:
            return dp[index][can_buy][k]

        if can_buy:
            dp[index][can_buy][k] = max(
                -prices[index] + solve(prices, index + 1, False, n, k, dp),
                solve(prices, index + 1, True, n, k, dp)
            )
        else:
            dp[index][can_buy][k] = max(
                prices[index] + solve(prices, index + 1, True, n, k - 1, dp),
                solve(prices, index + 1, False, n, k, dp)
            )
        return dp[index][can_buy][k]

    def best_time(prices, num_transactions):
        n = len(prices)
        dp = {i: {j: {k: None for k in range(num_transactions + 1)} for j in [True, False]} for i in range(n)}
        return solve(prices, 0, True, n, num_transactions, dp)

    print(best_time([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(best_time([1, 3, 1, 2, 4, 8], 2))
    print(best_time([5, 4, 3, 2, 1], 2))
    print(best_time([8, 5, 1, 3, 10], 2))
    print(best_time([2, 6, 5, 2], 0))
    print(best_time([1, 2, 3, 5], 2))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(n*k).
    """
    def best_time(prices, num_transactions):
        n = len(prices)
        dp = {i: {j: {k: 0 for k in range(num_transactions + 1)} for j in [True, False]} for i in range(n + 1)}
        for index in range(n - 1, -1, -1):
            for can_buy in [True, False]:
                for k in range(1, num_transactions + 1):
                    if can_buy:
                        dp[index][can_buy][k] = max(-prices[index] + dp[index + 1][False][k], dp[index + 1][True][k])
                    else:
                        dp[index][can_buy][k] = max(prices[index] + dp[index + 1][True][k - 1], dp[index + 1][False][k])
        return dp[0][True][num_transactions]

    print(best_time([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(best_time([1, 3, 1, 2, 4, 8], 2))
    print(best_time([5, 4, 3, 2, 1], 2))
    print(best_time([8, 5, 1, 3, 10], 2))
    print(best_time([2, 6, 5, 2], 0))
    print(best_time([1, 2, 3, 5], 2))


def space_optimized():
    """
        Time complexity is O(n*k) and space complexity is O(k).
    """
    def best_time(prices, num_transactions):
        n = len(prices)
        nxt = {j: {k: 0 for k in range(num_transactions + 1)} for j in [True, False]}
        for index in range(n - 1, -1, -1):
            curr = {j: {k: 0 for k in range(num_transactions + 1)} for j in [True, False]}
            for can_buy in [True, False]:
                for k in range(1, num_transactions + 1):
                    if can_buy:
                        curr[can_buy][k] = max(-prices[index] + nxt[False][k], nxt[True][k])
                    else:
                        curr[can_buy][k] = max(prices[index] + nxt[True][k - 1], nxt[False][k])
            nxt = curr
        return nxt[True][num_transactions]

    print(best_time([3, 3, 5, 0, 0, 3, 1, 4], 2))
    print(best_time([1, 3, 1, 2, 4, 8], 2))
    print(best_time([5, 4, 3, 2, 1], 2))
    print(best_time([8, 5, 1, 3, 10], 2))
    print(best_time([2, 6, 5, 2], 0))
    print(best_time([1, 2, 3, 5], 2))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()