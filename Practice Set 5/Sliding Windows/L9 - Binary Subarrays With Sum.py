# Problem link - https://leetcode.com/problems/binary-subarrays-with-sum/
# Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class Solution:
    @staticmethod
    def _get_less_than_equal_to(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).

            This method returns the count of subarrays whose sum <= k.
        """

        # if k is negative, return 0
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)

        # define result and tracking variables.
        _sum = count = 0

        # while there is ground to cover.
        while right < n:
            # add the right indexed value in sum
            _sum += arr[right]
            # while sum > k, shrink continuously from left
            while _sum > k:
                _sum -= arr[left]
                left += 1
            # if sum is within k, update the count variable
            if _sum <= k:
                count += (right - left + 1)
            # increment right index
            right += 1
        # return the count.
        return count

    @staticmethod
    def bin_subarray_count(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        return Solution._get_less_than_equal_to(arr, k) - Solution._get_less_than_equal_to(arr, k - 1)


print(Solution.bin_subarray_count([1, 0, 1, 0, 1], 2))
print(Solution.bin_subarray_count([0, 0, 0, 0, 0], 0))
print(Solution.bin_subarray_count([1, 0, 1, 1, 0, 1], 2))
print(Solution.bin_subarray_count([1, 1, 0, 1, 1], 5))
print(Solution.bin_subarray_count([1, 0, 1, 1, 1, 0, 1], 3))
