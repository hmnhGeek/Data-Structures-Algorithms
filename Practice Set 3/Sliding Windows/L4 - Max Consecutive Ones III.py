# Problem link - https://www.naukri.com/code360/problems/maximum-consecutive-ones_3843993
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def max_consecutive_1s(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define an edge case
        if k < 0:
            return
        # define window variables
        left = right = 0
        n = len(arr)

        # define result variables
        longest_length = 0
        start_index = -1

        # keep track of the 0s in the array.
        used_zeros = 0

        # while there is ground to cover.
        while right < n:
            # if right index element is 0, then increase the count of used_zeroes.
            if arr[right] == 0:
                used_zeros += 1

            # if you've breached the use of zeroes
            if used_zeros > k:
                # shrink from left
                if arr[left] == 0:
                    used_zeros -= 1
                left += 1

            # if use of zeroes is within k, update the result variables.
            if used_zeros <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right
            right += 1

        # return the final sub-array.
        return arr[start_index:start_index + longest_length] if start_index != -1 else []


print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_1s([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_1s([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_1s([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
