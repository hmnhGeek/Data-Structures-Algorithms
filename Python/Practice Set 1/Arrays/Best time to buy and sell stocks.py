# Problem link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Solution - https://www.youtube.com/watch?v=excAOvwF_Wk


class Solution:
    @staticmethod
    def find_max_profit(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        if len(arr) == 0:
            return
        max_profit = 0
        mini = arr[0]
        for i in range(1, len(arr)):
            profit = arr[i] - mini
            max_profit = max(max_profit, profit)
            mini = min(arr[i], mini)
        return max_profit


print(Solution.find_max_profit([7, 1, 5, 3, 6, 4]))
print(Solution.find_max_profit([7, 6, 4, 3, 1]))
print(Solution.find_max_profit([7, 10, 1, 3, 6, 9, 2]))
print(Solution.find_max_profit([1, 3, 6, 9, 11]))
print(Solution.find_max_profit([2, 100, 150, 120]))
print(Solution.find_max_profit([1, 2, 3, 4]))
print(Solution.find_max_profit([17, 20, 11, 9, 12, 6]))
print(Solution.find_max_profit([98, 101, 66, 72]))
