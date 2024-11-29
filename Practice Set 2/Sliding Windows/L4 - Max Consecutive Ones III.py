# Problem link - https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def max_consecutive_ones(arr, k):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # if k is 0 or negative, return
        if k <= 0:
            return

        # define window parameters
        left = right = 0
        n = len(arr)

        # define result variables.
        longest_length = 0
        start_index = -1

        # define a counter to track the number of zeros used.
        counter = k

        # while there is ground to cover.
        while right < n:
            # if the `right` indexed element is a 0, reduce counter by 1 to denote using this 0.
            if arr[right] == 0:
                counter -= 1

            # if used zeros > k, i.e., counter < 0, start decrement one unit from left
            if counter < 0:
                # if the `left` element is a 0, increase the counter value to denote a exclusion of this 0.
                if arr[left] == 0:
                    counter += 1
                left += 1
            else:
                # else, if the zeros used <= k, or, counter >= 0, update result variables.
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the result.
        return arr[start_index:start_index + longest_length] if start_index != -1 else -1


print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
