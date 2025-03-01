# Problem link - https://www.naukri.com/code360/problems/subarrays-with-at-most-k-distinct-values_1473804
# Solution - https://www.youtube.com/watch?v=7wYGbV_LsX4&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=11


class Solution:
    @staticmethod
    def _count_less_than_equal_to(arr, k):
        """
            Time complexity is O(n) and space is O(n).

            This method returns the count of subarrays with distinct integers count <= k.
        """

        # edge case
        if k < 0:
            return 0

        # define window variables.
        left = right = 0
        n = len(arr)

        # define tracking and result variables
        d = {i: 0 for i in arr}
        count = 0

        # while there is ground to cover.
        while right < n:
            # increment the count of right
            d[arr[right]] += 1

            # and while the count of distinct integers is more than k, shrink from left.
            while sum(1 for v in d.values() if v > 0) > k:
                d[arr[left]] -= 1
                left += 1

            # update the count of subarrays.
            if sum(1 for v in d.values() if v > 0) <= k:
                count += (right - left + 1)

            # increment right
            right += 1

        # return the count of subarrays.
        return count

    @staticmethod
    def get_subarray_count(arr, k):
        """
            Time complexity is O(2n) and space complexity is O(n).
        """

        return Solution._count_less_than_equal_to(arr, k) - Solution._count_less_than_equal_to(arr, k - 1)


print(Solution.get_subarray_count([2, 1, 1, 1, 3, 4, 3, 2], 3))
print(Solution.get_subarray_count([1, 2, 1, 2, 3], 2))
print(Solution.get_subarray_count([1, 2, 1, 3, 4], 3))
print(Solution.get_subarray_count([2, 1, 2, 1, 6], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 1))
print(Solution.get_subarray_count([2, 1, 3, 2, 4], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 4))
