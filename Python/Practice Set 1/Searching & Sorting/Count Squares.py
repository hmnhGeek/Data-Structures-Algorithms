# Problem link - https://www.geeksforgeeks.org/problems/count-squares3649/1


from math import sqrt, floor


class Solution:
    @staticmethod
    def count(n):
        """
            Time complexity is O(sqrt(n)) and space complexity is O(1).
        """
        return floor(sqrt(n - 1))


print(Solution.count(9))
print(Solution.count(3))
