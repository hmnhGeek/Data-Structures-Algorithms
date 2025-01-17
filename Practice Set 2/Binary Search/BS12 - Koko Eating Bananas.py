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
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """

        # at min len(arr) hours will be taken by koko to eat all the bananas.
        n = len(arr)
        if h < n:
            return -1
        # define search space
        # the min rate possible can be 1 banana/hr
        # the max rate can be max(arr) bananas/hr
        low, high = 1, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # in O(n) time find the hours taken to eat all bananas at mid-rate.
            can_eat_in_time = Solution._can_eat(arr, mid, h)
            # if koko can eat within h hours, then we can try with reduced rate
            if can_eat_in_time:
                high = mid - 1
            else:
                # else, we need to increase the rate to catch up.
                low = mid + 1
        # low will point to the correct answer.
        return low


print(Solution.koko([3, 6, 7, 11], 8))
print(Solution.koko([3, 6, 2, 8], 7))
print(Solution.koko([7, 15, 6, 3], 8))
print(Solution.koko([25, 12, 8, 14, 19], 5))
print(Solution.koko([30, 11, 23, 4, 20], 5))
print(Solution.koko([30, 11, 23, 4, 20], 6))
