# Problem link - https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1


from collections import Counter


class Solution:
    @staticmethod
    def is_subset(a, b):
        """
            Time complexity is O(n + m) and space complexity is O(n + m).
        """
        x, y = dict(Counter(a)), dict(Counter(b))
        for k in y:
            if k not in x:
                return False
            if x[k] < y[k]:
                return False
        return True


print(Solution.is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))
print(Solution.is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))
print(Solution.is_subset([10, 5, 2, 23, 19], [19, 5, 3]))
print(Solution.is_subset([2, 1, 8, 6, 4, 9, 3], [3, 4, 7]))
