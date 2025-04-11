# Problem link - https://www.naukri.com/code360/problems/maximum-consecutive-ones_3843993
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case
        if k < 0:
            return -1

        # define window parameters
        n = len(arr)
        left = right = 0

        # define result variables
        start_index = -1
        longest_length = 0

        # define tracking variables
        count_of_zeros = 0

        # while there is ground to cover.
        while right < n:
            # if right indexed value is 0, increment the zero count.
            if arr[right] == 0:
                count_of_zeros += 1

            # if you've breached the zero count, shrink just one unit from left.
            if count_of_zeros > k:
                if arr[left] == 0:
                    count_of_zeros -= 1
                left += 1

            # if not yet breached, update the result variables.
            if count_of_zeros <= k:
                start_index = left
                longest_length = max(right - left + 1, longest_length)

            # increment the right index.
            right += 1

        # return the subarray with max consecutive ones.
        return arr[start_index:start_index+longest_length] if start_index != -1 else []


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))

