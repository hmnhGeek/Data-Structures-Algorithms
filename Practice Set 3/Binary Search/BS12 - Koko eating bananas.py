from math import ceil


class Solution:
    @staticmethod
    def _hours_taken(arr, mid):
        hours = 0
        for i in range(len(arr)):
            hours += ceil(arr[i]/mid)
        return hours

    @staticmethod
    def koko(arr, h):
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            hours_taken = Solution._hours_taken(arr, mid)
            if hours_taken < h:
                high = mid - 1
            elif hours_taken == h:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.koko([3, 6, 7, 11], 8))
print(Solution.koko([3, 6, 2, 8], 7))
print(Solution.koko([7, 15, 6, 3], 8))
print(Solution.koko([25, 12, 8, 14, 19], 5))
print(Solution.koko([30, 11, 23, 4, 20], 5))
print(Solution.koko([30, 11, 23, 4, 20], 6))
