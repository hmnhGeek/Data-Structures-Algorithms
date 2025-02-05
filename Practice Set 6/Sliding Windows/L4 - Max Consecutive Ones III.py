# Problem link - https://www.naukri.com/code360/problems/maximum-consecutive-ones_3843993
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def max_consecutive_1s(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case
        if k < 0:
            return []

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variable
        zero_count = 0

        # define result variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover...
        while right < n:
            # increment the zero count if needed.
            if arr[right] == 0:
                zero_count += 1

            # shrink just one unit from left if needed.
            if zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1

            # update the result variables.
            if zero_count <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment the right index.
            right += 1

        # return the sub-array.
        return arr[start_index:start_index+longest_length] if start_index != -1 else []


print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_1s([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_1s([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
