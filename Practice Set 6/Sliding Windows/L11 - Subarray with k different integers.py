class Solution:
    @staticmethod
    def _get_count_less_than(arr, k):
        """
            Time complexity is O(n) and space is O(n).

            This method returns the count of subarrays with distinct integers count <= k.
        """

        if k < 0:
            return 0

        left = right = 0
        count = 0
        d = {i: 0 for i in arr}
        n = len(arr)

        while right < n:
            d[arr[right]] += 1
            while sum(1 for v in d.values() if v > 0) > k:
                d[arr[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v > 0) <= k:
                count += (right - left + 1)
            right += 1

        return count

    @staticmethod
    def get_subarray_count(arr, k):
        """
            Time complexity is O(2n) and space complexity is O(n).
        """
        return Solution._get_count_less_than(arr, k) - Solution._get_count_less_than(arr, k - 1)


print(Solution.get_subarray_count([2, 1, 1, 1, 3, 4, 3, 2], 3))
print(Solution.get_subarray_count([1, 2, 1, 2, 3], 2))
print(Solution.get_subarray_count([1, 2, 1, 3, 4], 3))
print(Solution.get_subarray_count([2, 1, 2, 1, 6], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 1))
print(Solution.get_subarray_count([2, 1, 3, 2, 4], 2))
print(Solution.get_subarray_count([1, 2, 3, 4, 5], 4))
