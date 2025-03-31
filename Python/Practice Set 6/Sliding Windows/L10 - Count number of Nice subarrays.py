# Problem link - https://leetcode.com/problems/count-number-of-nice-subarrays/
# Solution - https://www.youtube.com/watch?v=j_QOv9OT9Og&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=10


class Solution:
    @staticmethod
    def _get_count_less_than_equal_to(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)

        # store the count of odd numbers and the count of subarray where odd-count <= k.
        count_odds = 0
        count = 0

        # while there is ground to cover...
        while right < n:
            # increment the count of odd numbers accordingly.
            count_odds += arr[right] % 2

            # while the count of odd numbers > k, shrink continuously from left.
            while count_odds > k:
                count_odds -= arr[left] % 2
                left += 1

            # if the count of odd numbers <= k, increment the count of subarray.
            if count_odds <= k:
                count += (right - left + 1)

            # increment right index.
            right += 1

        # return the count.
        return count

    @staticmethod
    def get_nice_subarray_count(arr, k):
        """
            Overall time complexity is O(2n) and space complexity is O(1).
        """
        return Solution._get_count_less_than_equal_to(arr, k) - Solution._get_count_less_than_equal_to(arr, k - 1)


print(Solution.get_nice_subarray_count([1, 5, 2, 1, 1], 3))
print(Solution.get_nice_subarray_count([2, 4, 6], 1))
print(Solution.get_nice_subarray_count([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.get_nice_subarray_count([2, 5, 6, 9], 2))
print(Solution.get_nice_subarray_count([2, 2, 5, 6, 9, 2, 11], 2))
