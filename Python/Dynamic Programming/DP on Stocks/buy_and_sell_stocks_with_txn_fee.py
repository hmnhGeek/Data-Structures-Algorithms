# Problem link - https://www.naukri.com/code360/problems/rahul-and-his-chocolates_3118974?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=k4eK-vEmnKg&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=42


def buy_and_sell(stock_prices_day_wise, transaction_fee):
    # Overall time complexity is O(n) and space is O(1)
    # The idea is to levy the transaction fee either on selling time or on buying time (both
    # approaches work, you can pick any).

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

            # if there is a possibility to not buy, then we have 2 cases: 1. you sell (and deduct transaction fee)
            # and move on next index with can_buy set to True as you can now buy on upcoming days. 2. You don't do
            # anything, simply move to next day with same possibility of can_buy set as False. Finally, return the
            # max profit out of these 2 cases.
            else:
                curr[can_buy] = max(stock_prices_day_wise[i] - transaction_fee + nxt[True], 0 + nxt[False])
        nxt = curr

    # on the 0th day, denoted by nxt, you have the option to buy, and that's why passing it as True. This variable
    # is not `should_buy` but `can_buy`; basically, it just denotes a possibility. Thus, no need to
    # take max(can_buy = False, can_buy = True).
    return nxt[True]


print(buy_and_sell([1, 2, 3], 1))
print(buy_and_sell([1, 3, 5, 6], 2))