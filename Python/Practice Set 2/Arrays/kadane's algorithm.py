# Problem link - https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1


class Solution:
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    @staticmethod
    def kadane(arr):
        max_sum = -1e6
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            max_sum = max(max_sum, curr)
            if curr < 0:
                curr = 0
        return max_sum


print(Solution.kadane([2, 3, -8, 7, -1, 2, 3]))
print(Solution.kadane([-2, -4]))
print(Solution.kadane([5, 4, 1, 7, 8]))
print(Solution.kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
