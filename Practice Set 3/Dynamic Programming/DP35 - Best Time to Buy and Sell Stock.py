class Solution:
    @staticmethod
    def best_time(arr):
        profit = 0
        min_amt = arr[0]
        for i in range(1, len(arr)):
            profit = max(profit, arr[i] - min_amt)
            min_amt = min(min_amt, arr[i])
        return profit
    

print(Solution.best_time([7, 1, 5, 3, 6, 4]))
print(Solution.best_time([2, 100, 150, 120]))
print(Solution.best_time([1, 2, 3, 4]))
print(Solution.best_time([2, 2, 2, 2]))
print(Solution.best_time([17, 20, 11, 9, 12, 6]))
print(Solution.best_time([98, 101, 66, 72]))
print(Solution.best_time([7, 6, 4, 3, 1]))
print(Solution.best_time([1, 3, 6, 9, 11]))
print(Solution.best_time([7, 10, 1, 3, 6, 9, 2]))
