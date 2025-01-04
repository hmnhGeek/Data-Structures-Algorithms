class Solution:
    @staticmethod
    def _collect_wood(arr, mid):
        collected = 0
        for i in range(len(arr)):
            if arr[i] > mid:
                collected += (arr[i] - mid)
        return collected

    @staticmethod
    def get_max_ht(arr, k):
        if k > sum(arr) or k <= 0:
            return -1
        n = len(arr)
        low, high = 0, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            wood_collected = Solution._collect_wood(arr, mid)
            if wood_collected == k:
                low = mid + 1
            elif wood_collected < k:
                high = mid - 1
            else:
                low = mid + 1
        return high


print(Solution.get_max_ht([20, 15, 10, 17], 7))
print(Solution.get_max_ht([4, 42, 40, 26, 46], 20))
