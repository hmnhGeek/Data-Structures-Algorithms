class Solution:
    @staticmethod
    def _find_days(arr, mid):
        days = 0
        capacity_used = 0
        n = len(arr)
        for i in range(n):
            if capacity_used + arr[i] > mid:
                days += 1
                capacity_used = arr[i]
            else:
                capacity_used += arr[i]
        if capacity_used > 0:
            days += 1
            capacity_used = 0
        return days

    @staticmethod
    def get_least_ship_capacity(arr, k):
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
