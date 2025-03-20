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
        if k <= 0:
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            days = Solution._find_days(arr, mid)
            if days <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))
