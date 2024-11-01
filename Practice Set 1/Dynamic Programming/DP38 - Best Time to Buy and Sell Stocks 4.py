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


recursive()