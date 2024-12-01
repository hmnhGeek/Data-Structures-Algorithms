class Solution:
    @staticmethod
    def find_max_profit(arr):
        n = len(arr)
        if n <= 1:
            return 0
        mini = arr[0]
        profit = 0
        for i in range(1, n):
            profit = max(profit, arr[i] - mini)
            mini = min(mini, arr[i])
        return profit


print(Solution.find_max_profit([7, 1, 5, 3, 6, 4]))
print(Solution.find_max_profit([7, 6, 4, 3, 1]))
print(Solution.find_max_profit([7, 10, 1, 3, 6, 9, 2]))
print(Solution.find_max_profit([1, 3, 6, 9, 11]))
print(Solution.find_max_profit([2, 100, 150, 120]))
print(Solution.find_max_profit([1, 2, 3, 4]))
print(Solution.find_max_profit([17, 20, 11, 9, 12, 6]))
print(Solution.find_max_profit([98, 101, 66, 72]))
