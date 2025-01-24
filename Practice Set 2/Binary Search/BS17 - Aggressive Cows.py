class Solution:
    @staticmethod
    def aggressive_cows(arr, k):
        if k <= 0 or k > len(arr):
            return -1
        arr.sort()
        low, high = 0, max(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            cows_placed = Solution._get_cows_placed(arr, mid)

            if cows_placed < k:
                high = mid - 1
            else:
                low = mid + 1
        return high

    @staticmethod
    def _get_cows_placed(arr, mid):
        cows_placed = 1
        last_at = 0
        n = len(arr)
        for i in range(1, n):
            if arr[i] - arr[last_at] >= mid:
                cows_placed += 1
                last_at = i
        return cows_placed


print(Solution.aggressive_cows([0, 3, 4, 7, 9, 10], 4))
print(Solution.aggressive_cows([1, 2, 3], 2))
print(Solution.aggressive_cows([4, 2, 1, 3, 6], 2))
print(Solution.aggressive_cows([1, 2, 4, 8, 9], 3))
print(Solution.aggressive_cows([10, 1, 2, 7, 5], 3))
print(Solution.aggressive_cows([2, 12, 11, 3, 26, 7], 5))
print(Solution.aggressive_cows([6, 7,  9, 11, 13, 15], 4))
