class Solution:
    @staticmethod
    def get_min(arr):
        low, high = 0, len(arr) - 1
        ans = 1e6
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                ans = min(ans, arr[mid])
                high = mid - 1
        return ans


print(Solution.get_min([3, 4, 5, 1, 2]))
print(Solution.get_min([1, 2, 3, 4]))