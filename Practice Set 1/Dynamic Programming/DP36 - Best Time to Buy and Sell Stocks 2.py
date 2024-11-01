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


recursive()
print()
memoized()
