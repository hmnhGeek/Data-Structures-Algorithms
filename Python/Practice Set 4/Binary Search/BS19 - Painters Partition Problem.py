class Solution:
    @staticmethod
    def painter_partition(arr, k):
        if k > len(arr):
            return
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            painters_used = Solution._get_painters_used_count(arr, mid)
            if painters_used <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def _get_painters_used_count(arr, mid):
        painters = 0
        wall_painted = 0
        for i in range(len(arr)):
            if wall_painted + arr[i] > mid:
                painters += 1
                wall_painted = arr[i]
            else:
                wall_painted += arr[i]
        if wall_painted > 0:
            painters += 1
        return painters


print(Solution.painter_partition([10, 20, 30, 40], 2))
print(Solution.painter_partition([2, 1, 5, 6, 2, 3], 2))
print(Solution.painter_partition([48, 90], 2))
print(Solution.painter_partition([5, 10, 30, 20, 15], 3))
print(Solution.painter_partition([5]*4, 2))
