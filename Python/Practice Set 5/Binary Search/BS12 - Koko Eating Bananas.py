from math import ceil


class Solution:
    @staticmethod
    def koko(arr, hr):
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            time_taken = Solution._find_time_taken(arr, mid)
            if time_taken > hr:
                low = mid + 1
            else:
                high = mid - 1
        return low

    @staticmethod
    def _find_time_taken(arr, mid):
        n = len(arr)
        t = 0
        for i in range(n):
            t += ceil(arr[i]/mid)
        return t


print(Solution.koko([3, 6, 7, 11], 8))
print(Solution.koko([3, 6, 2, 8], 7))
print(Solution.koko([7, 15, 6, 3], 8))
print(Solution.koko([25, 12, 8, 14, 19], 5))
print(Solution.koko([30, 11, 23, 4, 20], 5))
print(Solution.koko([30, 11, 23, 4, 20], 6))