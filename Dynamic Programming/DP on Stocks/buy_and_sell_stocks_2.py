def recursive():
    def get_max_profit(prices, i, n, can_buy):
        # if you flow outside the list, there is no profit to be made.
        if i == n:
            return 0

        # if there is a possibility to buy, then we have 2 cases:
        # 1. you buy and move on next index with can_buy set to False as you cannot buy further until you sell the
        #      current one.
        # 2. You don't do anything, simply move to next day with same possibility of can_buy set as True.
        # Finally, return the max profit out of these 2 cases.
        if can_buy:
            profit = max(
                -prices[i] + get_max_profit(prices, i + 1, n, False),
                0 + get_max_profit(prices, i + 1, n, True)
            )

        # if there is a possibility to not buy, then we have 2 cases:
        # 1. you sell and move on next index with can_buy set to True as you can now buy on upcoming days.
        # 2. You don't do anything, simply move to next day with same possibility of can_buy set as False.
        # Finally, return the max profit out of these 2 cases.
        else:
            profit = max(
                prices[i] + get_max_profit(prices, i + 1, n, True),
                0 + get_max_profit(prices, i + 1, n, False)
            )

        # return the max profit that can be made out of these 4 scenarios.
        return profit

    def buy_and_sell(stock_prices_day_wise):
        # Overall time complexity is exponential and space is O(n).

        num_days = len(stock_prices_day_wise)
        # on the 0th day, you have the option to buy, and that's why passing it as True. This variable
        # is not `should_buy` but `can_buy`; basically, it just denotes a possibility. Thus, no need to
        # take max(can_buy = False, can_buy = True).
        return get_max_profit(stock_prices_day_wise, 0, num_days, True)

    print(buy_and_sell([1, 2, 3, 4, 5, 6, 7]))
    print(buy_and_sell([7, 6, 5, 4, 3, 2, 1]))
    print(buy_and_sell([1, 2, 3, 4, 5]))


recursive()
