class Solution:
    @staticmethod
    def circular_tour(gas, cost):
        n = len(gas)
        deficit = balance = start = 0
        for i in range(n):
            balance += gas[i] - cost[i]
            if balance < 0:
                deficit += balance
                start = i + 1
                balance = 0
        if deficit + balance >= 0:
            return start
        return -1


print(Solution.circular_tour([4, 6, 7, 4], [6, 5, 3, 5]))
print(Solution.circular_tour([6, 3, 7], [4, 6, 3]))