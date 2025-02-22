class Solution:
    @staticmethod
    def best_time(arr):
        # store the first day's price as min cost price for now.
        min_amt = arr[0]

        # assume the profit to be 0.
        profit = 0

        # loop from the second index till n - 1 index
        for i in range(1, len(arr)):
            # update the max profit
            profit = max(profit, arr[i] - min_amt)
            # also update the min cost price, to ensure that we always buy at min price.
            min_amt = min(min_amt, arr[i])
        # return the max profit.
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
