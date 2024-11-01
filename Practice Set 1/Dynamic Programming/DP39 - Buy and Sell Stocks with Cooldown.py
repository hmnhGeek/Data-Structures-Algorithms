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


recursive()