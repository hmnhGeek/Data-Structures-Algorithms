# Problem link - https://www.naukri.com/code360/problems/maximum-consecutive-ones_3843993
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        n = len(arr)
        left = right = length = 0
        start_index = -1
        zeros_used = 0
        while right < n:
            if arr[right] == 0:
                zeros_used += 1
            if zeros_used > k:
                if arr[left] == 0:
                    zeros_used -= 1
                left += 1
            if right - left + 1 > length:
                length = right - left + 1
                start_index = left
            right += 1
        if start_index != -1:
            return arr[start_index:start_index+length]
        return []


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))