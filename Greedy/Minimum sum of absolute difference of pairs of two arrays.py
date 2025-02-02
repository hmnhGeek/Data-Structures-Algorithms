# Problem link - https://www.geeksforgeeks.org/minimum-sum-absolute-difference-pairs-two-arrays/


class Solution:
    @staticmethod
    def solve(a1, a2):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """

        if len(a1) != len(a2):
            return 1e6
        a1.sort()
        a2.sort()
        _sum = 0
        for i in range(len(a1)):
            _sum += abs(a1[i] - a2[i])
        return _sum


print(Solution.solve([4, 1, 8, 7], [2, 3, 6, 5]))
