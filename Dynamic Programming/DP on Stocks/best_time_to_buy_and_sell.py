# Problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Solution - https://www.youtube.com/watch?v=excAOvwF_Wk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=36


def get_right_maximums(prices):
    # Overall time and space complexity is O(n) and O(n) respectively.

    # store a max value for reference, initialized to minimum price value = 0.
    max_val = 0

    # store a result array with all days having 0 as the max selling price.
    result = [0 for i in range(len(prices))]

    # loop on the prices array from right to left.
    for i in range(-1, -len(prices) - 1, -1):
        # if the selling price on ith day is less than the max selling price, then set result[i]
        # to max selling price because that will yield more profit.
        if prices[i] < max_val:
            result[i] = max_val
        # else if the price at ith day is more than the max selling price, we must update the max
        # selling price and nothing needs to be done on result array as there is no better price
        # to sell at after this index (or day).
        else:
            max_val = prices[i]

    # return the right maximums
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
