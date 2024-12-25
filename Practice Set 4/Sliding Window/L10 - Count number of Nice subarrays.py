# Problem link - https://leetcode.com/problems/count-number-of-nice-subarrays/description/
# Solution - https://www.youtube.com/watch?v=j_QOv9OT9Og&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=10


class Solution:
    @staticmethod
    def _count_less_than_equal_to(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)

        # define tracking variables
        _sum = count = 0

        # while there is ground to cover
        while right < n:
            # add 1 to sum if it is an odd number else add 0.
            _sum += arr[right] % 2

            # while sum has breached k limit, shrink from left continuously.
            while _sum > k:
                _sum -= arr[left] % 2
                left += 1

            # if sum is within k bound, update the count.
            if _sum <= k:
                count += (right - left + 1)

            # increment right index.
            right += 1

        # return the count of sub-arrays whose odd number count is <= k.
        return count

    @staticmethod
    def count_nice_subarrays(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        return Solution._count_less_than_equal_to(arr, k) - Solution._count_less_than_equal_to(arr, k - 1)


print(Solution.count_nice_subarrays([1, 1, 2, 1, 1], 3))
print(Solution.count_nice_subarrays([2, 4, 6], 1))
print(Solution.count_nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.count_nice_subarrays([2, 5, 6, 9], 2))
print(Solution.count_nice_subarrays([2, 2, 5, 6, 9, 2, 11], 2))
