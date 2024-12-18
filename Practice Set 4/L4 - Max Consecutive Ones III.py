# Problem link - https://leetcode.com/problems/max-consecutive-ones-iii/
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def max_consecutive_ones(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(arr)
        left = right = 0

        # define result variables
        longest_length = 0
        start_index = -1

        # define a tracker for the count of zeroes used.
        count_zeroes = 0

        # while there is ground to cover.
        while right < n:
            # if the right indexed element is 0, increment the count of 0s.
            if arr[right] == 0:
                count_zeroes += 1

            # if the count of zeroes has surpassed k, shrink one unit from left
            if count_zeroes > k:
                # if left indexed element is 0, decrement the count of 0.
                if arr[left] == 0:
                    count_zeroes -= 1
                left += 1

            # if count of zeroes is within k, update the result variables
            if count_zeroes <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment the right index.
            right += 1

        # return the subarray.
        return arr[start_index:start_index + longest_length] if start_index != -1 else []


print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
