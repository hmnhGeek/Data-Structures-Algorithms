from math import ceil


class Solution:
    @staticmethod
    def _hours_taken(arr, mid):
        # get the hours in O(n) time.
        hours = 0
        for i in range(len(arr)):
            hours += ceil(arr[i]/mid)
        return hours

    @staticmethod
    def koko(arr, h):
        """
            Time complexity is O(n * log(max(arr))) and space complexity is O(1).
        """

        # define the search space.
        low, high = 1, max(arr)

        # typical binary search
        while low <= high:
            # get the mid-rate.
            mid = int(low + (high - low)/2)

            # get the hours taken by koko to consume all the bananas at mid-rate.
            hours_taken = Solution._hours_taken(arr, mid)

            # if hours taken < h, then we can try even for a lower rate.
            if hours_taken < h:
                high = mid - 1

            # same case when hours taken = h
            elif hours_taken == h:
                high = mid - 1

            # otherwise, we must increase the rate.
            else:
                low = mid + 1

        # low points to the correct rate.
        return low


print(Solution.koko([3, 6, 7, 11], 8))
print(Solution.koko([3, 6, 2, 8], 7))
print(Solution.koko([7, 15, 6, 3], 8))
print(Solution.koko([25, 12, 8, 14, 19], 5))
print(Solution.koko([30, 11, 23, 4, 20], 5))
print(Solution.koko([30, 11, 23, 4, 20], 6))
