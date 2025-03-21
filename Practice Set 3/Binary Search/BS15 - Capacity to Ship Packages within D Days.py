# Problem link - https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379
# Solution - https://www.youtube.com/watch?v=MG-Ac4TAvTY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


class Solution:
    @staticmethod
    def _find_days(arr, mid):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # initially days consumed and capacity used will be 0.
        days = 0
        capacity_used = 0
        n = len(arr)

        # loop in the array
        for i in range(n):
            # if adding the current package to the ship breaches its capacity, increment the day count.
            if capacity_used + arr[i] > mid:
                days += 1
                # reset the used capacity now to the current package.
                capacity_used = arr[i]
            else:
                # else load the package on the ship
                capacity_used += arr[i]

        # if at the end the capacity is still > 0, then days must be incremented by 1.
        if capacity_used > 0:
            days += 1
            capacity_used = 0

        # return the number of days.
        return days

    @staticmethod
    def get_least_ship_capacity(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        # if the required number of days <= 0, return -1.
        if k <= 0:
            return -1

        # define the search space.
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)

            # count the number of days taken by the ship of capacity `mid` to ship all the packages in O(n) time.
            days = Solution._find_days(arr, mid)

            # if the days taken <= k, we can try for even lower capacity ship.
            if days <= k:
                high = mid - 1
            else:
                # else we must increase the ship capacity.
                low = mid + 1

        # low points to the correct answer.
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))
