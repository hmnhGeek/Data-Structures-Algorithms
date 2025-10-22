# Problem link - https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1


class Solution:
    @staticmethod
    def get_value(arr):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        result = []
        for i in range(len(arr)):
            if i + 1 == arr[i]:
                result.append(arr[i])
        return result


print(Solution.get_value([15, 2, 45, 4, 7]))
print(Solution.get_value([1]))
