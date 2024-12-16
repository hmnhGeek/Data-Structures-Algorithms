class Solution:
    @staticmethod
    def _less_than_equal_to_count(arr, k):
        """
            This method returns the count of sub-arrays where odd number count <= k.

            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case: if k is negative return 0.
        if k < 0:
            return 0

        # define window variables
        left = right = 0
        n = len(arr)
        _sum = count = 0

        # while there is ground to cover.
        while right < n:
            # if right is odd, add 1 else 0
            _sum += (arr[right] % 2)
            # while sum has breached k, shrink from left
            while _sum > k:
                _sum -= (arr[left] % 2)
                left += 1
            # update the count once _sum is within <= k.
            count += (right - left + 1)
            # increment right.
            right += 1
        # return the count of sub-arrays where odd number count <= k.
        return count

    @staticmethod
    def get_nice_subarray_count(arr, k):
        # Returns the count of sub-arrays where odd number count == k in O(2n) time and O(1) space.
        return Solution._less_than_equal_to_count(arr, k) - Solution._less_than_equal_to_count(arr, k - 1)


print(Solution.get_nice_subarray_count([1, 5, 2, 1, 1], 3))
print(Solution.get_nice_subarray_count([2, 4, 6], 1))
print(Solution.get_nice_subarray_count([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
print(Solution.get_nice_subarray_count([2, 5, 6, 9], 2))
print(Solution.get_nice_subarray_count([2, 2, 5, 6, 9, 2, 11], 2))
