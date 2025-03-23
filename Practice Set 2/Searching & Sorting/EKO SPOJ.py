class Solution:
    @staticmethod
    def _wood_collected(arr, mid):
        n = len(arr)
        wood = 0
        for i in range(n):
            if arr[i] > mid:
                wood += arr[i] - mid
        return wood

    @staticmethod
    def eko(arr, k):
        if k < 0:
            return -1
        low = 0
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            wood_collected = Solution._wood_collected(arr, mid)
            if wood_collected >= k:
                low = mid + 1
            else:
                high = mid - 1
        return high


print(Solution.eko([20, 15, 10, 17], 7))
print(Solution.eko([4, 42, 40, 26, 46], 20))
