def recursive():
    def solve_for_profit(stock_prices, day, total_days, can_buy, count_transactions):
        if count_transactions == 2:
            return 0

        if day == total_days:
            return 0

        if can_buy:
            return max(
                -stock_prices[day] + solve_for_profit(
                    stock_prices, day + 1, total_days, False, count_transactions
                ),
                solve_for_profit(
                    stock_prices, day + 1, total_days, True, count_transactions
                )
            )
        else:
            return max(
                stock_prices[day] + solve_for_profit(
                    stock_prices, day + 1, total_days, True, count_transactions + 1
                ),
                solve_for_profit(
                    stock_prices, day + 1, total_days, False, count_transactions
                )
            )

    def buy_sell_max_2_times(stock_prices):
        num_days = len(stock_prices)
        num_transactions_done = 0
        return solve_for_profit(stock_prices, 0, num_days, True, num_transactions_done)

    print(buy_sell_max_2_times([3, 3, 5, 0, 3, 1, 4]))
    print(buy_sell_max_2_times([1, 3, 1, 2, 4, 8]))
    print(buy_sell_max_2_times([5, 4, 3, 2, 1]))
    print(buy_sell_max_2_times([1, 2, 3, 4, 5]))
    print(buy_sell_max_2_times([3, 8, 2, 1, 6, 9, 2]))


recursive()