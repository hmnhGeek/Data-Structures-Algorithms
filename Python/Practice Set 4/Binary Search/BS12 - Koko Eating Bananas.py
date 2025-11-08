from math import ceil


class Solution:
    @staticmethod
    def koko(arr, h):
        n = len(arr)
        if h < n:
            return -1
        low = 1
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            time_consumed = Solution._find_time_consumed(arr, mid, h)
            if time_consumed > h:
                low = mid + 1
            else:
                high = mid - 1
        return low

    @staticmethod
    def _find_time_consumed(arr, mid, h):
        time_consumed = 0
        for i in arr:
            time_consumed += ceil(i/mid)
        return time_consumed


print(Solution.koko([3, 6, 7, 11], 8))
print(Solution.koko([3, 6, 2, 8], 7))
print(Solution.koko([7, 15, 6, 3], 8))
print(Solution.koko([25, 12, 8, 14, 19], 5))
print(Solution.koko([30, 11, 23, 4, 20], 5))
print(Solution.koko([30, 11, 23, 4, 20], 6))
