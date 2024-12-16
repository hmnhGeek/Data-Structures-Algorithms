class Solution:
    @staticmethod
    def get_min(arr):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[low] >= arr[mid] and arr[high] >= arr[mid]:
                return arr[mid]
            if arr[low] <= arr[high]:
                high = mid - 1
            elif arr[low] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return arr[low] if 0 <= low <= len(arr) - 1 else -1


print(Solution.get_min([4, 1, 2, 3]))
print(Solution.get_min([3, 4, 5, 1, 2]))
print(Solution.get_min([3, 4, 1, 2]))
print(Solution.get_min([25, 30, 5, 10, 15, 20]))
print(Solution.get_min([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_min([11, 13, 15, 17]))
