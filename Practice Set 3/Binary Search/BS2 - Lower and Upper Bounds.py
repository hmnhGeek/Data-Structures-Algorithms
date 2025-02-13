class Solution:
    @staticmethod
    def get_lower_bound(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        return low if low in range(len(arr)) else -1

    @staticmethod
    def get_upper_bound(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return low if low in range(len(arr)) else -1


print("Lower Bound")
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 5))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 8))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 9))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 800))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 2))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 0))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], -10))

print()

print("Upper Bound")
print(Solution.get_upper_bound([3, 5, 8, 15, 19], 5))
print(Solution.get_upper_bound([3, 5, 8, 15, 19], 8))
print(Solution.get_upper_bound([3, 5, 8, 15, 19], 9))
print(Solution.get_upper_bound([3, 5, 8, 15, 19], 800))
print(Solution.get_upper_bound([3, 5, 8, 15, 19], 2))
print(Solution.get_upper_bound([1, 2, 2, 3, 3, 5], 0))
print(Solution.get_upper_bound([1, 2, 2, 3, 3, 5], -10))