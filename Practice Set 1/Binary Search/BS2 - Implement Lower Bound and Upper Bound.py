class Solution:
    @staticmethod
    def get_lower_bound(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.get_lower_bound([3, 5, 8, 15, 19], 10))
print(Solution.get_lower_bound([1, 2, 2, 3], 0))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 0))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 2))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 7))
