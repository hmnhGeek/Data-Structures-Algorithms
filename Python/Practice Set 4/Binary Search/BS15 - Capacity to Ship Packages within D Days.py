# Problem link - https://www.naukri.com/code360/problems/capacity-to-ship-packages-within-d-days_1229379
# Solution - https://www.youtube.com/watch?v=MG-Ac4TAvTY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


class Solution:
    @staticmethod
    def get_least_ship_capacity(arr, threshold):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        # threshold cannot be negative or 0.
        if threshold <= 0:
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            days_taken = Solution.find_days_to_ship(arr, mid)
            if days_taken <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def find_days_to_ship(arr, mid):
        days_taken = 0
        capacity = 0
        i = 0
        while i < len(arr):
            capacity += arr[i]
            if capacity > mid:
                capacity = 0
                days_taken += 1
                continue
            i += 1
        if capacity > 0:
            days_taken += 1
            capacity = 0
        return days_taken


print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(Solution.get_least_ship_capacity([5, 4, 5, 2, 3, 4, 5, 6], 5))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.get_least_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(Solution.get_least_ship_capacity([3, 2, 2, 4, 1, 4], 3))
print(Solution.get_least_ship_capacity([1, 2, 3, 1, 1], 4))
