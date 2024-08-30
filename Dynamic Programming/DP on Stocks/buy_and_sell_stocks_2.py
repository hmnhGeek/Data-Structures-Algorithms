def recursive():
    def get_max_profit(prices, i, n, can_buy):
        if i == n:
            return 0

        if can_buy:
            profit = max(
                -prices[i] + get_max_profit(prices, i + 1, n, False),
                0 + get_max_profit(prices, i + 1, n, True)
            )
        else:
            profit = max(
                prices[i] + get_max_profit(prices, i + 1, n, True),
                0 + get_max_profit(prices, i + 1, n, False)
            )
        return profit

    def buy_and_sell(stock_prices_day_wise):
        num_days = len(stock_prices_day_wise)
        return get_max_profit(stock_prices_day_wise, 0, num_days, True)

    print(buy_and_sell([1, 2, 3, 4, 5, 6, 7]))
    print(buy_and_sell([7, 6, 5, 4, 3, 2, 1]))


recursive()