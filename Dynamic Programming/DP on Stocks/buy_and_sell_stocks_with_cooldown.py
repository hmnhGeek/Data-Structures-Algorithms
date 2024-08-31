def recursive():
    def solve(stock_prices, day, num_days, can_buy):
        # since we are using day + 2 in recursion, if we sell at last day, we will exceed num_days;
        # hence >=.
        if day >= num_days:
            return 0

        if can_buy:
            return max(
                -stock_prices[day] + solve(stock_prices, day + 1, num_days, False),
                solve(stock_prices, day + 1, num_days, True)
            )
        else:
            # in case of selling, use day + 2 (one day consumed for cooldown)
            return max(
                stock_prices[day] + solve(stock_prices, day + 2, num_days, True),
                solve(stock_prices, day + 1, num_days, False)
            )

    def sell_stock(stock_prices):
        # Time complexity is exponential and space is O(n).
        num_days = len(stock_prices)
        return solve(stock_prices, 0, num_days, True)

    print(sell_stock([4, 9, 0, 4, 10]))
    print(sell_stock([1, 2, 3, 4]))
    print(sell_stock([5, 4, 3]))


recursive()