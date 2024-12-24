class Solution:
    @staticmethod
    def _sum_less_than(arr, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(arr)
        _sum = count = 0
        while right < n:
            _sum += arr[right]
            while _sum > k:
                _sum -= arr[left]
                left += 1
            if _sum <= k:
                count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def bin_subarray_count(arr, k):
        return Solution._sum_less_than(arr, k) - Solution._sum_less_than(arr, k - 1)


print(Solution.bin_subarray_count([1, 0, 1, 0, 1], 2))
print(Solution.bin_subarray_count([0, 0, 0, 0, 0], 0))
