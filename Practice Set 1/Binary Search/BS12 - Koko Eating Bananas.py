# Problem link - https://www.naukri.com/code360/problems/minimum-rate-to-eat-bananas_7449064
# Solution - https://www.youtube.com/watch?v=qyfekrNni90&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=13


import math


class Solution:
    @staticmethod
    def _koko_can_eat(arr, mid, hrs):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        consumed_hrs = 0
        for i in range(len(arr)):
            consumed_hrs += math.ceil(arr[i] / mid)
        return consumed_hrs <= hrs

    @staticmethod
    def koko(arr, hrs):
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """

        if hrs <= 0:
            return -1

        # the min rate possible can be 1 banana/hr
        low = 1
        # the max rate can be max(arr) bananas/hr
        high = max(arr)

        # binary search...
        while low <= high:
            mid = int(low + (high - low) / 2)
            # in O(n) time, check if it is possible for koko to eat all the bananas within threshold hours.
            is_possible = Solution._koko_can_eat(arr, mid, hrs)

            # if it is possible, maybe we can slow down the rate
            if is_possible:
                high = mid - 1
            else:
                # else we must increase the rate.
                low = mid + 1

        # return the `low` value pointing to the minimum rate at which Koko can eat all the bananas within threshold
        # time.
        return low


print(Solution.koko([3, 6, 7, 11], 8))
print(Solution.koko([3, 6, 2, 8], 7))
print(Solution.koko([7, 15, 6, 3], 8))
print(Solution.koko([25, 12, 8, 14, 19], 5))
print(Solution.koko([30, 11, 23, 4, 20], 5))
print(Solution.koko([30, 11, 23, 4, 20], 6))
