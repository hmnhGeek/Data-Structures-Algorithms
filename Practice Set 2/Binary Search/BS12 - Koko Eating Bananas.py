from math import ceil


class Solution:
    @staticmethod
    def _can_eat(arr, mid, h):
        hours = 0
        for i in range(len(arr)):
            hours += ceil(arr[i]/mid)
        return hours <= h

    @staticmethod
    def koko(arr, h):
        n = len(arr)
        if h < n:
            return -1
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            can_eat_in_time = Solution._can_eat(arr, mid, h)
            if can_eat_in_time:
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

