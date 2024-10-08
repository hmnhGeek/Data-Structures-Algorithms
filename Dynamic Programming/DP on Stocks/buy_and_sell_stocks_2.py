# Problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Solution - https://www.youtube.com/watch?v=nGJmxkUJQGs&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=39


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


def memoized():
    def get_max_profit(prices, i, n, can_buy, dp):
        # if you flow outside the list, there is no profit to be made.
        if i == n:
            return 0

        if dp[i][can_buy] is not None:
            return dp[i][can_buy]

        # if there is a possibility to buy, then we have 2 cases:
        # 1. you buy and move on next index with can_buy set to False as you cannot buy further until you sell the
        #      current one.
        # 2. You don't do anything, simply move to next day with same possibility of can_buy set as True.
        # Finally, return the max profit out of these 2 cases.
        if can_buy:
            dp[i][can_buy] = max(
                -prices[i] + get_max_profit(prices, i + 1, n, False, dp),
                0 + get_max_profit(prices, i + 1, n, True, dp)
            )

        # if there is a possibility to not buy, then we have 2 cases:
        # 1. you sell and move on next index with can_buy set to True as you can now buy on upcoming days.
        # 2. You don't do anything, simply move to next day with same possibility of can_buy set as False.
        # Finally, return the max profit out of these 2 cases.
        else:
            dp[i][can_buy] = max(
                prices[i] + get_max_profit(prices, i + 1, n, True, dp),
                0 + get_max_profit(prices, i + 1, n, False, dp)
            )

        # return the max profit that can be made out of these 4 scenarios.
        return dp[i][can_buy]

    def buy_and_sell(stock_prices_day_wise):
        # Overall time complexity is O(n) and space is O(n + n) (one n for stack space, one for dp).

        num_days = len(stock_prices_day_wise)
        dp = {i: {True: None, False: None} for i in range(num_days)}
        # on the 0th day, you have the option to buy, and that's why passing it as True. This variable
        # is not `should_buy` but `can_buy`; basically, it just denotes a possibility. Thus, no need to
        # take max(can_buy = False, can_buy = True).
        return get_max_profit(stock_prices_day_wise, 0, num_days, True, dp)

    print(buy_and_sell([1, 2, 3, 4, 5, 6, 7]))
    print(buy_and_sell([7, 6, 5, 4, 3, 2, 1]))
    print(buy_and_sell([1, 2, 3, 4, 5]))


def tabulation():
    def buy_and_sell(stock_prices_day_wise):
        # Overall time complexity is O(n) and space is O(n)

        num_days = len(stock_prices_day_wise)
        dp = {i: {True: 0, False: 0} for i in range(num_days + 1)}

        # notice the direction of tabulation code.
        for i in range(num_days - 1, -1, -1):
            for can_buy in dp[i]:
                # if there is a possibility to buy, then we have 2 cases: 1. you buy and move on next index with
                # can_buy set to False as you cannot buy further until you sell the current one. 2. You don't do
                # anything, simply move to next day with same possibility of can_buy set as True. Finally,
                # return the max profit out of these 2 cases.
                if can_buy:
                    dp[i][can_buy] = max(-stock_prices_day_wise[i] + dp[i + 1][False], 0 + dp[i + 1][True])

                # if there is a possibility to not buy, then we have 2 cases:
                # 1. you sell and move on next index with can_buy set to True as you can now buy on upcoming days.
                # 2. You don't do anything, simply move to next day with same possibility of can_buy set as False.
                # Finally, return the max profit out of these 2 cases.
                else:
                    dp[i][can_buy] = max(stock_prices_day_wise[i] + dp[i + 1][True], 0 + dp[i + 1][False])

        # on the 0th day, you have the option to buy, and that's why passing it as True. This variable
        # is not `should_buy` but `can_buy`; basically, it just denotes a possibility. Thus, no need to
        # take max(can_buy = False, can_buy = True).
        return dp[0][True]

    print(buy_and_sell([1, 2, 3, 4, 5, 6, 7]))
    print(buy_and_sell([7, 6, 5, 4, 3, 2, 1]))
    print(buy_and_sell([1, 2, 3, 4, 5]))


def space_optimized():
    def buy_and_sell(stock_prices_day_wise):
        # Overall time complexity is O(n) and space is O(1)

        num_days = len(stock_prices_day_wise)

        # instead of using prev as name, use name `nxt` denoting next because this time our tabulation direction is
        # from n -> 0.
        nxt = {True: 0, False: 0}

        # notice the direction of tabulation code.
        for i in range(num_days - 1, -1, -1):
            curr = {True: 0, False: 0}
            for can_buy in [True, False]:
                # if there is a possibility to buy, then we have 2 cases: 1. you buy and move on next index with
                # can_buy set to False as you cannot buy further until you sell the current one. 2. You don't do
                # anything, simply move to next day with same possibility of can_buy set as True. Finally,
                # return the max profit out of these 2 cases.
                if can_buy:
                    curr[can_buy] = max(-stock_prices_day_wise[i] + nxt[False], 0 + nxt[True])

                # if there is a possibility to not buy, then we have 2 cases:
                # 1. you sell and move on next index with can_buy set to True as you can now buy on upcoming days.
                # 2. You don't do anything, simply move to next day with same possibility of can_buy set as False.
                # Finally, return the max profit out of these 2 cases.
                else:
                    curr[can_buy] = max(stock_prices_day_wise[i] + nxt[True], 0 + nxt[False])
            nxt = curr

        # on the 0th day, denoted by nxt, you have the option to buy, and that's why passing it as True. This variable
        # is not `should_buy` but `can_buy`; basically, it just denotes a possibility. Thus, no need to
        # take max(can_buy = False, can_buy = True).
        return nxt[True]

    print(buy_and_sell([1, 2, 3, 4, 5, 6, 7]))
    print(buy_and_sell([7, 6, 5, 4, 3, 2, 1]))
    print(buy_and_sell([1, 2, 3, 4, 5]))


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
