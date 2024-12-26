class Solution:
    @staticmethod
    def _num_gas_stations_placed(arr, mid, n):
        count = 0
        for i in range(n - 1):
            gas_stations = (arr[i + 1] - arr[i]) // mid
            if gas_stations * mid == arr[i + 1] - arr[i]:
                gas_stations -= 1
            count += gas_stations
        return count

    @staticmethod
    def minimize_distance(arr, k):
        if k <= 0:
            return
        low = 0
        high = 0
        n = len(arr)
        for i in range(n - 1):
            high = max(high, arr[i + 1] - arr[i])

        delta = 1e-6
        while high - low > delta:
            mid = (low + high) / 2
            num_placed = Solution._num_gas_stations_placed(arr, mid, n)
            if num_placed > k:
                low = mid
            else:
                high = mid
        return high


print(Solution.minimize_distance([1, 2, 3, 4, 5, 6, 7], 6))
print(Solution.minimize_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
print(Solution.minimize_distance([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2))
print(Solution.minimize_distance([1, 13, 17, 23], 5))
