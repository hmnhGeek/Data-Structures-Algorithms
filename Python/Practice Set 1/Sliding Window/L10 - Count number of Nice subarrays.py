# Problem link - https://leetcode.com/problems/count-number-of-nice-subarrays/
# Solution - https://www.youtube.com/watch?v=j_QOv9OT9Og&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=10


class Solution:
    @staticmethod
    def _count_nice_subarray(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        if k < 0:
            return 0

        # define the window variables.
        left = right = 0
        n = len(arr)

        # store the count of odd numbers
        odd_num_count = 0

        # store the number of substrings where odd count <= k.
        count_less_than_equal_to_k = 0

        # while there is ground to cover.
        while right < n:
            # increment the odd number count
            odd_num_count += (arr[right] % 2)

            # if the odd number count is > k, shrink from the left
            while odd_num_count > k:
                odd_num_count -= (arr[left] % 2)
                left += 1

            # update the number of substrings and increment right.
            count_less_than_equal_to_k += (right - left + 1)
            right += 1

        # return the count of such substrings.
        return count_less_than_equal_to_k

    @staticmethod
    def count_nice_subarray(arr, k):
        return Solution._count_nice_subarray(arr, k) - Solution._count_nice_subarray(arr, k - 1)


print(Solution.count_nice_subarray([1, 1, 2, 1, 1], 3))
print(Solution.count_nice_subarray([2, 4, 6], 1))
print(Solution.count_nice_subarray([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.count_nice_subarray([2, 2, 5, 6, 9, 2, 11], 2))
print(Solution.count_nice_subarray([2, 5, 6, 9], 2))
