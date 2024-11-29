class Solution:
    @staticmethod
    def _is_possible(arr, mid, days):
        """
            This will take O(n) time and O(1) space.
        """

        # assume consumed days and capacity to be 0.
        consumed_days = 0
        consumed_capacity = 0

        # start iterating on the packages.
        i = 0
        while i < len(arr):
            # let's see if we add the current day's package, will it overflow the ship's capacity or not.
            if consumed_capacity + arr[i] > mid:
                # if it does, then we can say that this package must go on the next day. We can then simply increment
                # the consumed days and set back the consumed ship capacity to 0, denoting that the ship is ready for
                # next day. Notice that we do not increment `i` as we still need to ship this package.
                consumed_days += 1
                consumed_capacity = 0
            else:
                # otherwise, simply load this package on the ship and move to the next package.
                consumed_capacity += arr[i]
                i += 1

        # finally, if there is still some package left on the ship, it will take yet another day to ship it.
        if consumed_capacity > 0:
            consumed_days += 1
            # finally, ship gets emptied.
            consumed_capacity = 0

        # return True if it was possible to ship all the packages within required days, else return False.
        return consumed_days <= days

    @staticmethod
    def get_least_ship_capacity(arr, days):
        """
            Overall time complexity is O(n * log(sum(arr))) and space complexity is O(1).
        """

        # let low be the minimum assumed capacity, i.e., 1 unit capacity.
        # let high be the capacity of the ship equal to sum of all the packages. This would mean that the ship will be
        # able to ship all the packages in 1 day.
        low, high = 1, sum(arr)

        # Typical binary search
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._is_possible(arr, mid, days)
            # if it is possible to ship all the packages with `mid` capacity within `days` days, let's try to check for
            # some lower capacity.
            if is_possible:
                high = mid - 1
            else:
                # Otherwise, if it's not possible, then we must increase the capacity.
                low = mid + 1

        # return `low` which points to the least capacity that is required to ship all the packages within `days` days.
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))