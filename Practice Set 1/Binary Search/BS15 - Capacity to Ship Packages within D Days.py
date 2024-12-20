# Problem link - https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379
# Solution - https://www.youtube.com/watch?v=MG-Ac4TAvTY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


class Solution:
    @staticmethod
    def _is_possible(arr, mid, d):
        capacity_used = 0
        days_used = 0

        # loop on all the packages.
        for i in range(len(arr)):
            # if the ith package itself has weight more than ship capacity, then return False.
            if arr[i] > mid:
                return False

            # if the ith package on being added to the ship still <= mid, then add the package.
            if arr[i] + capacity_used <= mid:
                capacity_used += arr[i]
            else:
                # else ship the previous i - 1 packages in one day and set ith package on the ship for next day.
                capacity_used = arr[i]
                days_used += 1

        # if there is still some capacity used on the ship, take one another day to ship.
        if 0 < capacity_used <= mid:
            days_used += 1

        # return true if used number of days <= d.
        return days_used <= d

    @staticmethod
    def get_least_ship_capacity(arr, d):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        # if required days count is 0 or negative, return -1.
        if d <= 0:
            return -1

        # define a search space for ship capacity.
        low, high = max(arr), sum(arr)

        # binary search
        while low <= high:
            mid = int(low + (high - low)/2)
            # check if it is possible to ship all packages within d days if capacity of the ship is mid.
            is_possible = Solution._is_possible(arr, mid, d)

            # if it is possible, then lets try to check with some lower capacity ship
            if is_possible:
                high = mid - 1
            else:
                # else we must increase the capacity of the ship.
                low = mid + 1

        # return low, which points to the least capacity such that all the packages can be shipped in d days.
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))