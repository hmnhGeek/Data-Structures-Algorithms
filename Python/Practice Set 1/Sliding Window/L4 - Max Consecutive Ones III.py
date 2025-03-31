# Problem link - https://leetcode.com/problems/max-consecutive-ones-iii/description/
# Solution - https://www.youtube.com/watch?v=3E4JBHSLpYk&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=4


class Solution:
    @staticmethod
    def get_max_consecutive_ones(arr, k):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # if k is negative, return nothing.
        if k < 0:
            return

        # initialize length of array into `n`.
        n = len(arr)

        # store the longest length to return; for now, make it 0.
        longest_length = 0

        # store a count variable to check if we have flipped k zeroes or not.
        count = 0

        # store a start index in order to return a sub-array.
        start_index = 0

        # store left and right pointers, both initialized 0 index at beginning.
        left, right = 0, 0

        # while there is ground to cover.
        while right < n:
            # if the `right` element is a 1, we can expand to the right.
            if arr[right] == 1:
                # update the longest length and start index with current `right` value.
                longest_length = max(longest_length, right - left + 1)
                start_index = left
                # expand the window to the right by one unit.
                right += 1
            elif count < k:
                # if it's not a 1, but a 0, and you've not flipped all k-zeroes yet, then assume that you have flipped
                # this zero and increment the `count` value.
                count += 1
                # now since it is a 1 now (after flipping), do the same thing as done in the `if` condition.
                longest_length = max(longest_length, right - left + 1)
                start_index = left
                right += 1
            else:
                # however, if it's a zero, and you've flipped all the k-zeroes, then we must shrink the window from the
                # left side. However, to do this, check if arr[left] is a 0 or not. Because if it is a 0, then we are
                # basically removing a 0 from our window, which means our count should decrement by 1 unit.
                if arr[left] == 0:
                    count -= 1
                # and anyway, since you're shrinking, increment `left`.
                left += 1

        # finally return the longest length of such a window and the window itself.
        return longest_length, arr[start_index:start_index+longest_length]


print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(Solution.get_max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(Solution.get_max_consecutive_ones([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(Solution.get_max_consecutive_ones([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))
