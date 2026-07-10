class Solution:
    @staticmethod
    def get_max_profit(arr):
        profit = 0
        buy = arr[0]
        for i in range(1, len(arr)):
            profit = max(profit, arr[i] - buy)
            buy = min(buy, arr[i])
        return profit
    

print(Solution.get_max_profit([7, 1, 5, 3, 6, 4]))
print(Solution.get_max_profit([2, 100, 150, 120]))
print(Solution.get_max_profit([1, 2, 3, 4]))
print(Solution.get_max_profit([2, 2, 2, 2]))
print(Solution.get_max_profit([17, 20, 11, 9, 12, 6]))
print(Solution.get_max_profit([98, 101, 66, 72]))
print(Solution.get_max_profit([7, 6, 4, 3, 1]))
print(Solution.get_max_profit([1, 3, 6, 9, 11]))
print(Solution.get_max_profit([7, 10, 1, 3, 6, 9, 2]))
