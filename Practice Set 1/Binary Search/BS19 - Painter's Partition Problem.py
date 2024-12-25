class Solution:
    @staticmethod
    def _is_possible(arr, mid, k):
        painters = 0
        time_consumed = 0
        for i in range(len(arr)):
            if arr[i] + time_consumed <= mid:
                time_consumed += arr[i]
            else:
                painters += 1
                time_consumed = arr[i]
        if time_consumed > 0:
            painters += 1
            time_consumed = 0
        if painters <= k:
            return 0
        return 1

    @staticmethod
    def painter_partition(arr, k):
        if k <= 0 or k > len(arr):
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._is_possible(arr, mid, k)
            if is_possible == 0:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.painter_partition([10, 20, 30, 40], 2))
print(Solution.painter_partition([2, 1, 5, 6, 2, 3], 2))
print(Solution.painter_partition([48, 90], 2))
print(Solution.painter_partition([5, 10, 30, 20, 15], 3))