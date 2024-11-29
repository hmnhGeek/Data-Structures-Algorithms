import math


class Solution:
    @staticmethod
    def _is_possible(arr, mid, threshold):
        _sum = 0
        for i in range(len(arr)):
            _sum += math.ceil(arr[i] / mid)
        return _sum <= threshold

    @staticmethod
    def smallest_divisor(arr, threshold):
        low = 1
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            is_possible = Solution._is_possible(arr, mid, threshold)
            if is_possible:
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
