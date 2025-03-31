# Problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Solution - https://www.youtube.com/watch?v=excAOvwF_Wk


class Solution:
    @staticmethod
    def find_max_profit(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(arr)

        # if there is only 1 or no day available to trade, return 0 profit.
        if n <= 1:
            return 0

        # set the minimum price to be first day's price.
        mini = arr[0]
        # set initial profit to 0.
        profit = 0

        # loop in the array from second day
        for i in range(1, n):
            # update the max profit by assuming that you sold on this day and brought it at min price of mini.
            profit = max(profit, arr[i] - mini)
            # also, update mini with current day's price.
            mini = min(mini, arr[i])

        # return max profit.
        return profit


print(Solution.find_max_profit([7, 1, 5, 3, 6, 4]))
print(Solution.find_max_profit([7, 6, 4, 3, 1]))
print(Solution.find_max_profit([7, 10, 1, 3, 6, 9, 2]))
print(Solution.find_max_profit([1, 3, 6, 9, 11]))
print(Solution.find_max_profit([2, 100, 150, 120]))
print(Solution.find_max_profit([1, 2, 3, 4]))
print(Solution.find_max_profit([17, 20, 11, 9, 12, 6]))
print(Solution.find_max_profit([98, 101, 66, 72]))
