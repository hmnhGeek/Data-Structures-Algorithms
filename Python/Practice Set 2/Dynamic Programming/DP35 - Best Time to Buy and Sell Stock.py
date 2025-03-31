# Problem link - https://www.naukri.com/code360/problems/stocks-are-profitable_893405?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=excAOvwF_Wk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=36


def max_profit(prices):
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    # store the last day's price as max selling price for now.
    sp = prices[-1]
    # assume the profit to be 0.
    profit = 0
    # loop from the second last index till 0th index
    for i in range(-2, -len(prices) - 1, -1):
        # get the earning by calculation sp - cp (on ith day)
        earning = sp - prices[i]
        # update the max profit
        profit = max(profit, earning)
        # also update the max selling price, to ensure that we always sell at max price.
        sp = max(sp, prices[i])
    # return the max profit.
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
