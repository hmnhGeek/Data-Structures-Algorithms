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


def memoized():
    def solve_for_profit(stock_prices, day, total_days, can_buy, count_transactions, dp):
        # if at most 2 transactions have been completed, there can't be any more profit, return 0.
        if count_transactions == 2:
            return 0

        # if you are out of bounds of the `stock_prices` array, no further profit can be made, return 0.
        if day == total_days:
            return 0

        if dp[day][can_buy][count_transactions] is not None:
            return dp[day][can_buy][count_transactions]

        # if there is a possibility to buy, then either buy it on this day or don't buy it. However, ensure that you
        # don't increase the transaction count; transaction count increases by 1 only when a stock is sold.
        if can_buy:
            dp[day][can_buy][count_transactions] = max(
                -stock_prices[day] + solve_for_profit(
                    stock_prices, day + 1, total_days, False, count_transactions, dp
                ),
                solve_for_profit(
                    stock_prices, day + 1, total_days, True, count_transactions, dp
                )
            )
        # if you cannot buy, try selling the stock. Remember, if you sell the stock, ensure to increase the transaction
        # count by 1, else, don't sell and continue to the next day with same transaction count.
        else:
            dp[day][can_buy][count_transactions] = max(
                stock_prices[day] + solve_for_profit(
                    stock_prices, day + 1, total_days, True, count_transactions + 1, dp
                ),
                solve_for_profit(
                    stock_prices, day + 1, total_days, False, count_transactions, dp
                )
            )
        return dp[day][can_buy][count_transactions]

    def buy_sell_max_2_times(stock_prices):
        # Time complexity of the recursive solution is O(n*2*3) and space complexity is O(n + 2*3*n). Remember that the
        # transaction limit is capped at 2. Had it been variable, then the time complexity would not be O(n).

        # get the number of days that we have the data for.
        num_days = len(stock_prices)

        # initially, there are no transactions that have completed.
        num_transactions_done = 0

        # initialize a 3D DP array for this memoized solution. We are passing 3 for `j` because count_transactions can
        # be 0, 1, 2.
        dp = {i: {True: {j: None for j in range(3)}, False: {j: None for j in range(3)}} for i in range(num_days)}

        # get the maximum profit by setting the possibility to buy on 0th day as True, with 0 transactions done till
        # now.
        return solve_for_profit(stock_prices, 0, num_days, True, num_transactions_done, dp)

    print(buy_sell_max_2_times([3, 3, 5, 0, 3, 1, 4]))
    print(buy_sell_max_2_times([1, 3, 1, 2, 4, 8]))
    print(buy_sell_max_2_times([5, 4, 3, 2, 1]))
    print(buy_sell_max_2_times([1, 2, 3, 4, 5]))
    print(buy_sell_max_2_times([3, 8, 2, 1, 6, 9, 2]))


def tabulation():
    def buy_sell_max_2_times(stock_prices):
        # Time complexity of the recursive solution is O(n*2*3) and space complexity is O(2*3*n). Remember that the
        # transaction limit is capped at 2. Had it been variable, then the time complexity would not be O(n).

        # get the number of days that we have the data for.
        num_days = len(stock_prices)

        # initialize a 3D DP array for this memoized solution. We are passing 3 for `j` because count_transactions can
        # be 0, 1, 2. Also, remember to use `num_days + 1` because in dp[day + 1], when you're on the last day (starting
        # point of the for-loop), `day + 1 = (num_days - 1) + 1 = num_days`. And this key must exist in dp so that we
        # don't get any error. Basically, it is the base case `day == num_days` and by default it is already set to 0.
        dp = {i: {True: {j: 0 for j in range(3)}, False: {j: 0 for j in range(3)}} for i in range(num_days + 1)}

        # start from the last day (opposite of memoization solution direction).
        for day in range(num_days - 1, -1, -1):
            for can_buy in [True, False]:
                # now, note that we don't want to start count_transactions from 2 because for 2 we would have to refer
                # key 3 (which does not exist). Anyway, for all count_transactions = 2, the value is already 0, and
                # this is one of the other base cases. And so, count_transactions + 1 = 1 + 1 = 2 won't create any
                # issues.
                for count_transactions in range(1, -1, -1):
                    # if there is a possibility to buy, then either buy it on this day or don't buy it. However,
                    # ensure that you don't increase the transaction count; transaction count increases by 1 only
                    # when a stock is sold.
                    if can_buy:
                        dp[day][can_buy][count_transactions] = max(
                            -stock_prices[day] + dp[day + 1][False][count_transactions],
                            dp[day + 1][True][count_transactions]
                        )
                    # if you cannot buy, try selling the stock. Remember, if you sell the stock, ensure to increase
                    # the transaction count by 1, else, don't sell and continue to the next day with same transaction
                    # count.
                    else:
                        dp[day][can_buy][count_transactions] = max(
                            stock_prices[day] + dp[day + 1][True][count_transactions + 1],
                            dp[day + 1][False][count_transactions]
                        )

        # get the maximum profit by setting the possibility to buy on 0th day as True, with 0 transactions done till
        # now.
        return dp[0][True][0]

    print(buy_sell_max_2_times([3, 3, 5, 0, 3, 1, 4]))
    print(buy_sell_max_2_times([1, 3, 1, 2, 4, 8]))
    print(buy_sell_max_2_times([5, 4, 3, 2, 1]))
    print(buy_sell_max_2_times([1, 2, 3, 4, 5]))
    print(buy_sell_max_2_times([3, 8, 2, 1, 6, 9, 2]))


recursive()
print()
memoized()
print()
tabulation()