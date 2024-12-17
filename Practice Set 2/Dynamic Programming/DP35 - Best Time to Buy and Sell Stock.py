def max_profit(prices):
    sp = prices[-1]
    profit = 0
    for i in range(-2, -len(prices) - 1, -1):
        earning = sp - prices[i]
        profit = max(profit, earning)
        sp = max(sp, prices[i])
    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([2, 100, 150, 120]))
print(max_profit([1, 2, 3, 4]))
print(max_profit([2, 2, 2, 2]))
print(max_profit([17, 20, 11, 9, 12, 6]))
print(max_profit([98, 101, 66, 72]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([1, 3, 6, 9, 11]))
print(max_profit([7, 10, 1, 3, 6, 9, 2]))
