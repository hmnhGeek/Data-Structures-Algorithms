# Problem link - https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variable
        zero_count = 0

        # define result variables
        max_length = 0
        start_index = -1

        # while there is ground to cover
        while right < n:
            # if right element is 0, increment 0 count.
            if arr[right] == 0:
                zero_count += 1

            # if zero count is breached, shrink one unit from left
            if zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            # if zero count is within limits, update the result variables
            if zero_count <= k:
                max_length = max(max_length, right - left + 1)
                start_index = left

            # increment right index
            right += 1

        # return the subarray.
        return arr[start_index:start_index+max_length] if start_index != -1 else []


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))