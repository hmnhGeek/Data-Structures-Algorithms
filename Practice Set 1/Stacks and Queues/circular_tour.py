# Problem link - https://www.geeksforgeeks.org/problems/circular-tour-1587115620/1
# Solution - https://www.youtube.com/watch?v=_gJ3to4RyeQ&t=5632s


class Solution:
    @staticmethod
    def circular_tour(gas, cost):
        # Time complexity is O(N) and space is O(1).
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