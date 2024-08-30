def get_right_maximums(prices):
    max_val = 0
    result = [0 for i in range(len(prices))]

    for i in range(-1, -len(prices) - 1, -1):
        if prices[i] < max_val:
            result[i] = max_val
        else:
            max_val = prices[i]

    return result


def best_time(prices):
    """
        Overall time complexity is O(n) and space complexity is O(n).
    """

    # for a given index we need to check for the maximum price that we can sell at post this index, and thus,
    # we need to find the right maximums for each index in the prices array. This will take O(n) time and
    # O(n) space.
    right_max = get_right_maximums(prices)

    # initially, assume the maximum profit to be 0
    max_profit = 0

    # now loop on indices of right_max (or prices array); basically index denotes the day.
    # This will take O(n) time.
    for i in range(len(right_max)):
        # update the maximum profit by taking maximum of existing max profit and the profit
        # that will be obtained on ith day.
        max_profit = max(max_profit, right_max[i] - prices[i])

    # return max profit that can be made.
    return max_profit


print(best_time([7, 1, 5, 3, 6, 4]))
print(best_time([2, 100, 150, 120]))
print(best_time([1, 2, 3, 4]))
print(best_time([2, 2, 2, 2]))
print(best_time([17, 20, 11, 9, 12, 6]))
print(best_time([98, 101, 66, 72]))
print(best_time([7, 6, 4, 3, 1]))
