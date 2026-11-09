class Solution:
    @staticmethod
    def get_least_ship_capacity(arr, threshold):
        if threshold <= 0:
            return -1
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._is_possible_to_ship(arr, mid, threshold)
            if is_possible:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def _is_possible_to_ship(arr, mid, threshold):
        days_used = 0
        weight_shipped = 0
        for i in range(len(arr)):
            weight = arr[i]
            weight_shipped += weight
            if weight_shipped > mid:
                days_used += 1
                weight_shipped = weight
        if weight_shipped > 0:
            weight_shipped = 0
            days_used += 1
        return days_used <= threshold


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))
