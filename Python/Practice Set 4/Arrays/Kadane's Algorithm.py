# Problem link - https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Solution - https://www.youtube.com/watch?v=HCL4_bOd3-4


class Solution:
    @staticmethod
    def kadane(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        curr_sum = 0
        max_sum = -1e6
        i = 0
        n = len(arr)
        while i < n:
            curr_sum += arr[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
            i += 1
        return max_sum


print(Solution.kadane([2, 3, -8, 7, -1, 2, 3]))
print(Solution.kadane([-2, -4]))
print(Solution.kadane([5, 4, 1, 7, 8]))
print(Solution.kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution.kadane([1]))
print(Solution.kadane([5, 4, -1, 7, 8]))
