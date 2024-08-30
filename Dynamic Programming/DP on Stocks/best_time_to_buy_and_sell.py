def get_right_maximums(prices):
    max_val = float('-inf')
    result = [float('-inf') for i in range(len(prices))]

    for i in range(-1, -len(prices) - 1, -1):
        if prices[i] < max_val:
            result[i] = max_val
        else:
            max_val = prices[i]

    return result


def best_time(prices):
    right_max = get_right_maximums(prices)
    max_profit = float('-inf')
    for i in range(len(right_max)):
        if right_max[i] != float('-inf'):
            max_profit = max(max_profit, right_max[i] - prices[i])
    return max_profit if max_profit != float('-inf') else 0


print(best_time([7, 1, 5, 3, 6, 4]))
print(best_time([ 2, 100, 150, 120]))
print(best_time([1, 2, 3, 4]))
print(best_time([2, 2, 2, 2]))
print(best_time([17, 20, 11, 9, 12, 6]))
print(best_time([98, 101, 66, 72]))