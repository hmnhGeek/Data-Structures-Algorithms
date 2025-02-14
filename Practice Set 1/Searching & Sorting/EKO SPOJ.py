class Solution:
    @staticmethod
    def _collect(arr, mid):
        w = 0
        for i in range(len(arr)):
            if arr[i] > mid:
                w += (arr[i] - mid)
        return w

    @staticmethod
    def solve(arr, w):
        low = 0
        high = max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            wood_collected = Solution._collect(arr, mid)
            if wood_collected == w:
                low = mid + 1
            elif wood_collected < w:
                high = mid - 1
            else:
                low = mid + 1
        return high


print(Solution.solve([20, 15, 10, 17], 7))
print(Solution.solve([4, 42, 40, 26, 46], 20))
