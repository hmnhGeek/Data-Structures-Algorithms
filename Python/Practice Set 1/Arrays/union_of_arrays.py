# Problem link - https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class Solution:
    @staticmethod
    def union(arr1, arr2):
        """
            Time complexity is O(n + m) and space complexity is O(n + m).
        """
        set1 = set(arr1)
        set2 = set(arr2)
        intersection = set1.intersection(set2)
        result = []
        for i in set1:
            if i not in intersection:
                result.append(i)
        for i in set2:
            if i not in intersection:
                result.append(i)
        for i in intersection:
            result.append(i)
        return result


print(Solution.union([1, 2, 3, 2, 1], [3, 2, 2, 3, 3, 2]))
print(Solution.union([1, 2, 3], [4, 5, 6]))
print(Solution.union([1, 2, 1, 1, 2], [2, 2, 1, 2, 1]))
