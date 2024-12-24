# Problem link - https://leetcode.com/problems/binary-subarrays-with-sum/
# Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class Solution:
    @staticmethod
    def _sum_less_than(arr, k):
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
            # increment sum
            _sum += arr[right]

            # if sum exceeds k, shrink from left
            while _sum > k:
                _sum -= arr[left]
                left += 1

            # if sum <= k, update count
            if _sum <= k:
                count += (right - left + 1)

            # increment right index
            right += 1

        # return the count of sub-arrays such that sum <= k.
        return count

    @staticmethod
    def bin_subarray_count(arr, k):
        """
            Time complexity is O(2n) and space complexity is O(1).
        """

        # return the count of sub arrays with sum == k.
        return Solution._sum_less_than(arr, k) - Solution._sum_less_than(arr, k - 1)


print(Solution.bin_subarray_count([1, 0, 1, 0, 1], 2))
print(Solution.bin_subarray_count([0, 0, 0, 0, 0], 0))
print(Solution.bin_subarray_count([1, 0, 1, 1, 0, 1], 2))
print(Solution.bin_subarray_count([1, 1, 0, 1, 1], 5))
print(Solution.bin_subarray_count([1, 0, 1, 1, 1, 0, 1], 3))
