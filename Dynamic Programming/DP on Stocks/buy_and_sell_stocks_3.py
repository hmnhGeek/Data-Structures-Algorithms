def recursive():
    def solve_for_profit(stock_prices, day, total_days, can_buy, count_transactions):
        # if at most 2 transactions have been completed, there can't be any more profit, return 0.
        if count_transactions == 2:
            return 0

        # if you are out of bounds of the `stock_prices` array, no further profit can be made, return 0.
        if day == total_days:
            return 0

        # if there is a possibility to buy, then either buy it on this day or don't buy it. However, ensure that you
        # don't increase the transaction count; transaction count increases by 1 only when a stock is sold.
        if can_buy:
            return max(
                -stock_prices[day] + solve_for_profit(
                    stock_prices, day + 1, total_days, False, count_transactions
                ),
                solve_for_profit(
                    stock_prices, day + 1, total_days, True, count_transactions
                )
            )
        # if you cannot buy, try selling the stock. Remember, if you sell the stock, ensure to increase the transaction
        # count by 1, else, don't sell and continue to the next day with same transaction count.
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
        # Time complexity of the recursive solution is O(2^n) and space complexity is O(n).

        # get the number of days that we have the data for.
        num_days = len(stock_prices)

        # initially, there are no transactions that have completed.
        num_transactions_done = 0

        # get the maximum profit by setting the possibility to buy on 0th day as True, with 0 transactions done till
        # now.
        return solve_for_profit(stock_prices, 0, num_days, True, num_transactions_done)

    print(buy_sell_max_2_times([3, 3, 5, 0, 3, 1, 4]))
    print(buy_sell_max_2_times([1, 3, 1, 2, 4, 8]))
    print(buy_sell_max_2_times([5, 4, 3, 2, 1]))
    print(buy_sell_max_2_times([1, 2, 3, 4, 5]))
    print(buy_sell_max_2_times([3, 8, 2, 1, 6, 9, 2]))


recursive()