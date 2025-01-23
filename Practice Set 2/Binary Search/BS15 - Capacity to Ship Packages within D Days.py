class Solution:
    @staticmethod
    def _get_days_used(arr, mid):
        days_consumed = 0
        capacity_used = 0
        for i in range(len(arr)):
            if capacity_used + arr[i] <= mid:
                capacity_used += arr[i]
            else:
                days_consumed += 1
                capacity_used = arr[i]
        if capacity_used > 0:
            days_consumed += 1
            capacity_used = 0
        return days_consumed

    @staticmethod
    def get_least_ship_capacity(arr, days):
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            num_days_taken = Solution._get_days_used(arr, mid)
            if num_days_taken > days:
                low = mid + 1
            elif num_days_taken == days:
                high = mid - 1
            else:
                high = mid - 1
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))
