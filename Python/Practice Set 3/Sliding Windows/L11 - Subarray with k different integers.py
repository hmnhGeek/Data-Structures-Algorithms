# Problem link - https://leetcode.com/problems/subarrays-with-k-different-integers/
# Solution - https://www.youtube.com/watch?v=7wYGbV_LsX4&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=11


class Solution:
    @staticmethod
    def _count_less_than_equal_to(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).

            The code is similar to L10 and L9.
        """

        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        count = 0
        d = {i: 0 for i in arr}
        while right < n:
            d[arr[right]] += 1
            # while the count of distinct integers > k, shrink from left
            while sum(1 for v in d.values() if v != 0) > k:
                d[arr[left]] -= 1
                left += 1
            count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_subarray_count(arr, k):
        """
            Time complexity is O(2n) and space complexity is O(1).
        """
        return Solution._count_less_than_equal_to(arr, k) - Solution._count_less_than_equal_to(arr, k - 1)


print(Solution.get_subarray_count([1, 2, 1, 3, 4], 3))
print(Solution.get_subarray_count([1,2,1,2,3], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 1))
print(Solution.get_subarray_count([2, 1, 3, 2, 4], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 4))
