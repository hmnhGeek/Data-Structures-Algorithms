"""
    Problem link - https://leetcode.com/problems/subarrays-with-k-different-integers/description/
    Solution - https://www.youtube.com/watch?v=7wYGbV_LsX4&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=11
    Please refer to comments in file L9. The problem is exactly same to that.
"""


class Solution:
    @staticmethod
    def _get_subarray_with_k_distinct_integers(arr, k):
        """
            Time complexity is O(n) and space complexity is O(n) for the dictionary.
        """

        if k < 0:
            return 0

        # window variables
        left = right = 0
        n = len(arr)
        count_less_than_equal_to_k = 0

        # bucket to store the count of all the integers in the window.
        bucket = {i: 0 for i in arr}
        while right < n:
            bucket[arr[right]] += 1

            # sum(1 for v in bucket.values() if v != 0) gives the count of integers present in the window.
            while sum(1 for v in bucket.values() if v != 0) > k:
                bucket[arr[left]] -= 1
                left += 1
            count_less_than_equal_to_k += (right - left + 1)
            right += 1
        return count_less_than_equal_to_k

    @staticmethod
    def get_subarray_with_k_distinct_integers(arr, k):
        return Solution._get_subarray_with_k_distinct_integers(arr,
                                                               k) - Solution._get_subarray_with_k_distinct_integers(arr,
                                                                                                                    k - 1)


print(Solution.get_subarray_with_k_distinct_integers([2, 1, 1, 1, 3, 4, 3, 2], 3))
print(Solution.get_subarray_with_k_distinct_integers([1, 2, 1, 2, 3], 2))
print(Solution.get_subarray_with_k_distinct_integers([1, 2, 1, 3, 4], 3))
print(Solution.get_subarray_with_k_distinct_integers([2, 1, 2, 1, 6], 2))
print(Solution.get_subarray_with_k_distinct_integers([1, 2, 3, 4, 5], 1))
print(Solution.get_subarray_with_k_distinct_integers([2, 1, 3, 2, 4], 2))
print(Solution.get_subarray_with_k_distinct_integers([1, 2, 3, 4, 5], 4))
