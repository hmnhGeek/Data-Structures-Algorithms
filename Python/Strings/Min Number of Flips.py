# Problem link - https://www.geeksforgeeks.org/problems/min-number-of-flips3210/1
# Solution - https://www.youtube.com/watch?v=F0E7k6X_kt8


class Solution:
    @staticmethod
    def get_min_flips(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        n = len(string)
        c1, c2 = 0, 0
        for i in range(n):
            if i % 2 == 0 and string[i] == '1':
                c1 += 1
            if i % 2 == 1 and string[i] == '0':
                c1 += 1
            if i % 2 == 0 and string[i] == '0':
                c2 += 1
            if i % 2 == 1 and string[i] == '1':
                c2 += 1
        return min(c1, c2)


print(Solution.get_min_flips("001"))
print(Solution.get_min_flips("0001010111"))
