class Solution:
    @staticmethod
    def _get_painters(arr, mid):
        painters = time = 0
        n = len(arr)
        for i in range(n):
            if time + arr[i] <= mid:
                time += arr[i]
            else:
                painters += 1
                time = arr[i]
        if time > 0:
            painters += 1
            time = 0
        return painters

    @staticmethod
    def painter_partition(arr, k):
        n = len(arr)
        if n < k:
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            painters = Solution._get_painters(arr, mid)
            if painters <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.painter_partition([10, 20, 30, 40], 2))
print(Solution.painter_partition([2, 1, 5, 6, 2, 3], 2))
print(Solution.painter_partition([48, 90], 2))
print(Solution.painter_partition([5, 10, 30, 20, 15], 3))
print(Solution.painter_partition([5]*4, 2))
