def recursive():
    def get_max_profit(stock_prices, day, total_days, can_buy, count_transactions, max_allowed_transactions):
        if count_transactions == max_allowed_transactions:
            return 0

        if day == total_days:
            return 0

        if can_buy:
            return max(
                -stock_prices[day] + get_max_profit(
                    stock_prices, day + 1, total_days, False, count_transactions, max_allowed_transactions
                ),
                get_max_profit(
                    stock_prices, day + 1, total_days, True, count_transactions, max_allowed_transactions
                )
            )
        else:
            return max(
                stock_prices[day] + get_max_profit(
                    stock_prices, day + 1, total_days, True, count_transactions + 1, max_allowed_transactions
                ),
                get_max_profit(
                    stock_prices, day + 1, total_days, False, count_transactions, max_allowed_transactions
                )
            )

    def get_maximum_profit_by_selling_stocks(stock_prices, max_allowed_transactions):
        # Time complexity is exponential and space complexity is O(n).
        num_days = len(stock_prices)
        return get_max_profit(stock_prices, 0, num_days, True, 0, max_allowed_transactions)

    print(
        get_maximum_profit_by_selling_stocks([3, 2, 6, 5, 0, 3], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks([8, 5, 1, 3, 10], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks([10, 8, 6, 2], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks([2, 6, 5, 2], 0)
    )

    print(
        get_maximum_profit_by_selling_stocks([1, 2, 3, 5], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [2, 4, 1], 2
        )
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [12, 14, 17, 10, 14, 13, 12, 15], 3
        )
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [100, 30, 15, 10, 8, 25, 80], 3
        )
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [90, 80, 70, 60, 50], 1
        )
    )


def memoized():
    def get_max_profit(stock_prices, day, total_days, can_buy, count_transactions, max_allowed_transactions, dp):
        if count_transactions == max_allowed_transactions:
            return 0

        if day == total_days:
            return 0

        if dp[day][can_buy][count_transactions] is not None:
            return dp[day][can_buy][count_transactions]

        if can_buy:
            dp[day][can_buy][count_transactions] = max(
                -stock_prices[day] + get_max_profit(
                    stock_prices, day + 1, total_days, False, count_transactions, max_allowed_transactions, dp
                ),
                get_max_profit(
                    stock_prices, day + 1, total_days, True, count_transactions, max_allowed_transactions, dp
                )
            )
        else:
            dp[day][can_buy][count_transactions] = max(
                stock_prices[day] + get_max_profit(
                    stock_prices, day + 1, total_days, True, count_transactions + 1, max_allowed_transactions, dp
                ),
                get_max_profit(
                    stock_prices, day + 1, total_days, False, count_transactions, max_allowed_transactions, dp
                )
            )
        return dp[day][can_buy][count_transactions]

    def get_maximum_profit_by_selling_stocks(stock_prices, max_allowed_transactions):
        # Time complexity is O(6n) and space complexity is O(7n).
        num_days = len(stock_prices)
        dp = {i: {True: {j: None for j in range(3)}, False: {j: None for j in range(3)}} for i in range(num_days)}
        return get_max_profit(stock_prices, 0, num_days, True, 0, max_allowed_transactions, dp)

    print(
        get_maximum_profit_by_selling_stocks([3, 2, 6, 5, 0, 3], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks([8, 5, 1, 3, 10], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks([10, 8, 6, 2], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks([2, 6, 5, 2], 0)
    )

    print(
        get_maximum_profit_by_selling_stocks([1, 2, 3, 5], 2)
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [2, 4, 1], 2
        )
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [12, 14, 17, 10, 14, 13, 12, 15], 3
        )
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [100, 30, 15, 10, 8, 25, 80], 3
        )
    )

    print(
        get_maximum_profit_by_selling_stocks(
            [90, 80, 70, 60, 50], 1
        )
    )


recursive()
print()
memoized()