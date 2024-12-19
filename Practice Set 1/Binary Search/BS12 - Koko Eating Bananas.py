import math

class Solution:
    @staticmethod
    def _koko_can_eat(arr, mid, hrs):
        consumed_hrs = 0
        for i in range(len(arr)):
            consumed_hrs += math.ceil(arr[i]/mid)
        return consumed_hrs <= hrs

    @staticmethod
    def koko(arr, hrs):
        if hrs <= 0:
            return -1
        low = 1
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._koko_can_eat(arr, mid, hrs)
            if is_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.koko([3, 6, 7, 11], 8))