class Solution:
    @staticmethod
    def min_in_uniques(arr):
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if 0 <= mid - 1 < n and arr[mid - 1] > arr[mid]:
                return arr[mid]
            if 0 <= mid + 1 < n and arr[mid + 1] < arr[mid]:
                return arr[mid + 1]
            if arr[low] > arr[mid]:
                high = mid - 1
            elif arr[high] < arr[mid]:
                low = mid + 1
            elif arr[low] <= arr[mid] <= arr[high]:
                high = mid - 1
        return arr[low] if low in range(n) else -1


print(Solution.min_in_uniques([4, 5, 6, 7, 0, 1, 2]))
print(Solution.min_in_uniques([4, 1, 2, 3]))
print(Solution.min_in_uniques([3, 4, 5, 1, 2]))
print(Solution.min_in_uniques([3, 4, 1, 2]))
print(Solution.min_in_uniques([25, 30, 5, 10, 15, 20]))
print(Solution.min_in_uniques([11, 13, 15, 17]))
