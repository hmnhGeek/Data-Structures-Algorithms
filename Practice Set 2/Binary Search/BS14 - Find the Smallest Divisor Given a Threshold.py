from math import ceil


class Solution:
    @staticmethod
    def _get_val(arr, mid):
        val = 0
        for i in range(len(arr)):
            val += ceil(arr[i]/mid)
        return val

    @staticmethod
    def smallest_divisor(arr, threshold):
        if threshold < len(arr):
            return -1
        n = len(arr)
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            val = Solution._get_val(arr, mid)
            if val <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.smallest_divisor([1, 2, 5, 9], 6))
print(Solution.smallest_divisor([1, 2, 3, 4, 5], 8))
print(Solution.smallest_divisor([8, 4, 2, 3], 10))
print(Solution.smallest_divisor([2, 3, 5, 7, 11], 11))
print(Solution.smallest_divisor([44, 22, 33, 11, 1], 5))
print(Solution.smallest_divisor([1, 1, 1, 1], 4))