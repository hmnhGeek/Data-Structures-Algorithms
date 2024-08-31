# Problem link - https://www.naukri.com/code360/problems/highway-billboards_3125969?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IGIe46xw3YY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=40


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


def memoized():
    def solve(stock_prices, day, num_days, can_buy, dp):
        # since we are using day + 2 in recursion, if we sell at last day, we will exceed num_days;
        # hence >=.
        if day >= num_days:
            return 0

        if dp[day][can_buy] is not None:
            return dp[day][can_buy]

        if can_buy:
            dp[day][can_buy] = max(
                -stock_prices[day] + solve(stock_prices, day + 1, num_days, False, dp),
                solve(stock_prices, day + 1, num_days, True, dp)
            )
        else:
            # in case of selling, use day + 2 (one day consumed for cooldown)
            dp[day][can_buy] = max(
                stock_prices[day] + solve(stock_prices, day + 2, num_days, True, dp),
                solve(stock_prices, day + 1, num_days, False, dp)
            )
        return dp[day][can_buy]

    def sell_stock(stock_prices):
        # Time complexity is O(2n) and space is O(3n).
        num_days = len(stock_prices)
        dp = {i: {True: None, False: None} for i in range(num_days + 2)}
        return solve(stock_prices, 0, num_days, True, dp)

    print(sell_stock([4, 9, 0, 4, 10]))
    print(sell_stock([1, 2, 3, 4]))
    print(sell_stock([5, 4, 3]))


def tabulation():
    def sell_stock(stock_prices):
        # Time complexity is O(2n) and space is O(2n).
        num_days = len(stock_prices)
        dp = {i: {True: 0, False: 0} for i in range(num_days + 2)}

        for day in range(num_days - 1, -1, -1):
            for can_buy in [True, False]:
                if can_buy:
                    dp[day][can_buy] = max(-stock_prices[day] + dp[day + 1][False], dp[day + 1][True])
                else:
                    # in case of selling, use day + 2 (one day consumed for cooldown)
                    dp[day][can_buy] = max(stock_prices[day] + dp[day + 2][True], dp[day + 1][False])
        return dp[0][True]

    print(sell_stock([4, 9, 0, 4, 10]))
    print(sell_stock([1, 2, 3, 4]))
    print(sell_stock([5, 4, 3]))


def space_optimized():
    def sell_stock(stock_prices):
        # Time complexity is O(2n) and space is O(4) = O(1).
        num_days = len(stock_prices)
        nxt = {True: 0, False: 0}
        nxt2nxt = {True: 0, False: 0}

        for day in range(num_days - 1, -1, -1):
            curr = {True: 0, False: 0}
            for can_buy in [True, False]:
                if can_buy:
                    curr[can_buy] = max(-stock_prices[day] + nxt[False], nxt[True])
                else:
                    # in case of selling, use day + 2 (one day consumed for cooldown)
                    curr[can_buy] = max(stock_prices[day] + nxt2nxt[True], nxt[False])
            nxt2nxt = nxt
            nxt = curr
        return nxt[True]

    print(sell_stock([4, 9, 0, 4, 10]))
    print(sell_stock([1, 2, 3, 4]))
    print(sell_stock([5, 4, 3]))


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
