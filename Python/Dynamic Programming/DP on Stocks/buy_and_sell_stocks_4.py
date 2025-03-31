# Problem link - https://www.naukri.com/code360/problems/best-time-to-buy-and-sell-stock_1080698?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IV1dHbk5CDc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=40

# Please refer to the buy_and_sell_stocks_3.py file for comments. This problem is same as that one.


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
        dp = {i: {True: {j: None for j in range(max_allowed_transactions + 1)}, False: {j: None for j in range(max_allowed_transactions + 1)}} for i in range(num_days)}
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


def tabulation():
    def get_maximum_profit_by_selling_stocks(stock_prices, max_allowed_transactions):
        # Time complexity is O(6n) and space complexity is O(6n).
        num_days = len(stock_prices)
        dp = {i: {True: {j: 0 for j in range(max_allowed_transactions + 1)}, False: {j: 0 for j in range(max_allowed_transactions + 1)}} for i in range(num_days + 1)}

        for day in range(num_days - 1, -1, -1):
            for can_buy in [True, False]:
                for count_transactions in range(max_allowed_transactions - 1, -1, -1):
                    if can_buy:
                        dp[day][can_buy][count_transactions] = max(
                            -stock_prices[day] + dp[day + 1][False][count_transactions],
                            dp[day + 1][True][count_transactions]
                        )
                    else:
                        dp[day][can_buy][count_transactions] = max(
                            stock_prices[day] + dp[day + 1][True][count_transactions + 1],
                            dp[day + 1][False][count_transactions]
                        )

        return dp[0][True][0]

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


def space_optimized():
    def get_maximum_profit_by_selling_stocks(stock_prices, max_allowed_transactions):
        # Time complexity is O(6n) and space complexity is O(6) = O(1).
        num_days = len(stock_prices)
        nxt = {True: {j: 0 for j in range(max_allowed_transactions + 1)}, False: {j: 0 for j in range(max_allowed_transactions + 1)}}

        for day in range(num_days - 1, -1, -1):
            curr = {True: {j: 0 for j in range(max_allowed_transactions + 1)}, False: {j: 0 for j in range(max_allowed_transactions + 1)}}
            for can_buy in [True, False]:
                for count_transactions in range(max_allowed_transactions - 1, -1, -1):
                    if can_buy:
                        curr[can_buy][count_transactions] = max(
                            -stock_prices[day] + nxt[False][count_transactions],
                            nxt[True][count_transactions]
                        )
                    else:
                        curr[can_buy][count_transactions] = max(
                            stock_prices[day] + nxt[True][count_transactions + 1],
                            nxt[False][count_transactions]
                        )
            nxt = curr

        return nxt[True][0]

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


print("Recursion Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()
