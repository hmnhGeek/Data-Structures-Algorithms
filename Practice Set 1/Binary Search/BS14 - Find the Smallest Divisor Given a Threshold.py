from math import ceil


class Solution:
    @staticmethod
    def _threshold_not_breached(arr, mid, threshold):
        val = 0
        for i in range(len(arr)):
            val += ceil(arr[i] / mid)
        return val <= threshold

    @staticmethod
    def find_smallest(arr, threshold):
        if threshold < len(arr):
            return -1
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low) / 2)
            is_possible = Solution._threshold_not_breached(arr, mid, threshold)
            if is_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.find_smallest([1, 2, 5, 9], 6))
print(Solution.find_smallest([1, 2, 3, 4, 5], 8))
print(Solution.find_smallest([8, 4, 2, 3], 10))
print(Solution.find_smallest([2, 3, 5, 7, 11], 11))
print(Solution.find_smallest([44, 22, 33, 11, 1], 5))
print(Solution.find_smallest([2, 3, 7, 4, 10], 5))
print(Solution.find_smallest([7, 3, 3, 6], 10))
print(Solution.find_smallest([1, 1, 1, 1], 4))
