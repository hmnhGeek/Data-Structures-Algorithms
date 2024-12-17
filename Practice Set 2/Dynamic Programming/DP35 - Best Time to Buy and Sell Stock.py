def max_profit(prices):
    sp = prices[-1]
    profit = 0
    for i in range(-2, -len(prices) - 1, -1):
        earning = sp - prices[i]
        profit = max(profit, earning)
        sp = max(sp, prices[i])
    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))