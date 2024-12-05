class Solution:
    @staticmethod
    def _get_painters(arr, mid):
        painters_used = 1
        units = arr[0]
        for i in range(1, len(arr)):
            if arr[i] + units <= mid:
                units += arr[i]
            else:
                painters_used += 1
                units = arr[i]
        return painters_used

    @staticmethod
    def painter(arr, k):
        if k > len(arr):
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            painters_used = Solution._get_painters(arr, mid)
            if painters_used <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.painter([2, 1, 5, 6, 2, 3], 2))
print(Solution.painter([10, 20, 30, 40], 2))
print(Solution.painter([48, 90], 2))
print(Solution.painter([5, 10, 30, 20, 15], 3))
print(Solution.painter([5, 5, 5, 5], 2))