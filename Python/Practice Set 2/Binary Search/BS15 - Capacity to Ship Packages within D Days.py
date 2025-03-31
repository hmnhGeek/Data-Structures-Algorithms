# Problem link - https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379
# Solution - https://www.youtube.com/watch?v=MG-Ac4TAvTY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


class Solution:
    @staticmethod
    def _get_days_used(arr, mid):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # assume no day is used and ship is empty.
        days_consumed = 0
        capacity_used = 0

        # loop on the packages
        for i in range(len(arr)):
            # if adding this package still keeps everything within threshold mid, then add this package on the ship.
            if capacity_used + arr[i] <= mid:
                capacity_used += arr[i]
            else:
                # else increase the day count
                days_consumed += 1
                # and add only this package to the ship now.
                capacity_used = arr[i]

        # at the end, if the ship has some packages, it would take another day.
        if capacity_used > 0:
            days_consumed += 1
            capacity_used = 0

        # return the consumed days.
        return days_consumed

    @staticmethod
    def get_least_ship_capacity(arr, days):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        # days must be positive.
        if days <= 0:
            return -1

        # minimum capacity of max weight element is required and max could be the sum of all the weights as that would
        # ship everything in just 1 day.
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # get the number of days to ship the packages if ship capacity is mid.
            num_days_taken = Solution._get_days_used(arr, mid)

            # if days taken is more than required, we must increase ship's capacity
            if num_days_taken > days:
                low = mid + 1

            # else, if it takes <= required days, then we can reduce the ship's capacity.
            elif num_days_taken == days:
                high = mid - 1
            else:
                high = mid - 1

        # return the minimum ship capacity required.
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))
