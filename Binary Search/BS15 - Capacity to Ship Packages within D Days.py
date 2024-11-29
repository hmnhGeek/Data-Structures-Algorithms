class Solution:
    @staticmethod
    def _is_possible(arr, mid, days):
        consumed_days = 0
        consumed_capacity = 0
        i = 0
        while i < len(arr):
            if consumed_capacity + arr[i] > mid:
                consumed_days += 1
                consumed_capacity = 0
            else:
                consumed_capacity += arr[i]
                i += 1
        if consumed_capacity > 0:
            consumed_days += 1
            consumed_capacity = 0
        return consumed_days <= days

    @staticmethod
    def get_least_ship_capacity(arr, days):
        low, high = 1, sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._is_possible(arr, mid, days)
            if is_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))