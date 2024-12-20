class Solution:
    @staticmethod
    def _is_possible(arr, mid, d):
        capacity_used = 0
        days_used = 0
        for i in range(len(arr)):
            if arr[i] > mid:
                return False
            if arr[i] + capacity_used <= mid:
                capacity_used += arr[i]
            else:
                capacity_used = arr[i]
                days_used += 1
        if capacity_used <= mid:
            days_used += 1
        return days_used <= d

    @staticmethod
    def get_least_ship_capacity(arr, d):
        if d <= 0:
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._is_possible(arr, mid, d)
            if is_possible:
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