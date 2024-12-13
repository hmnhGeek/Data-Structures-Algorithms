# Problem link - https://leetcode.com/problems/binary-subarrays-with-sum/description/
# Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class Solution:
    @staticmethod
    def _helper(arr, k):
        """
            This method returns the count of subarrays whose sum is <= k.

            Time: O(n) and space is O(1).
        """

        # if k is negative, return 0.
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)

        # define sum and count variables.
        _sum = count = 0

        # while there is ground to cover.
        while right < n:
            # add the right indexed value in to the sum
            _sum += arr[right]
            # while sum is greater than k, shrink continuously from left
            while _sum > k:
                _sum -= arr[left]
                left += 1
            # if sum is within k, update the count
            if _sum <= k:
                count += (right - left + 1)
            # increment right
            right += 1
        # return the count of subarrays where sum <= k.
        return count

    @staticmethod
    def solve(arr, k):
        # in O(2n) and O(1), return the count of subarrays where sum == k.
        return Solution._helper(arr, k) - Solution._helper(arr, k - 1)


print(Solution.solve([1, 0, 1, 0, 1], 2))
print(Solution.solve([0, 0, 0, 0, 0], 0))
print(Solution.solve([1, 0, 1, 1, 0, 1], 2))
print(Solution.solve([1, 1, 0, 1, 1], 5))
print(Solution.solve([1, 0, 1, 1, 1, 0, 1], 3))
