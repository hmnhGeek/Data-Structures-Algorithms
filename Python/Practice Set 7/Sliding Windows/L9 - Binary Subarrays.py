# Problem link - https://leetcode.com/problems/binary-subarrays-with-sum/
# Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class Solution:
    @staticmethod
    def get_less_than_equal_to_count(arr, k):
        if k < 0:
            return 0
        n = len(arr)
        left = right = 0
        _sum = 0
        count = 0
        while right < n:
            _sum += arr[right]
            while _sum > k:
                _sum -= arr[left]
                left += 1
            count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def bin_subarray_count(arr, k):
        # Time complexity is O(n) and space complexity is O(1).
        return Solution.get_less_than_equal_to_count(arr, k) - Solution.get_less_than_equal_to_count(arr, k - 1)


print(Solution.bin_subarray_count([1, 0, 1, 0, 1], 2))
print(Solution.bin_subarray_count([0, 0, 0, 0, 0], 0))
print(Solution.bin_subarray_count([1, 0, 1, 1, 0, 1], 2))
print(Solution.bin_subarray_count([1, 1, 0, 1, 1], 5))
print(Solution.bin_subarray_count([1, 0, 1, 1, 1, 0, 1], 3))
