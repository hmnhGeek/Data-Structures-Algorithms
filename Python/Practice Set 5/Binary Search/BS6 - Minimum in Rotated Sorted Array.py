class Solution:
    @staticmethod
    def get_min_in_rotated(arr):
        n = len(arr)
        low, high = 0, n - 1
        minimum = 1e6
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] == arr[mid] == arr[high]:
                minimum = min(minimum, arr[low])
                low += 1
                high -= 1
                continue
            if arr[low] <= arr[mid]:
                minimum = min(minimum, arr[low])
                low = mid + 1
            else:
                minimum = min(minimum, arr[mid])
                high = mid - 1
        return minimum


print(Solution.get_min_in_rotated([4, 5, 6, 7, 0, 1, 2]))
print(Solution.get_min_in_rotated([4, 1, 2, 3]))
print(Solution.get_min_in_rotated([3, 4, 5, 1, 2]))
print(Solution.get_min_in_rotated([3, 4, 1, 2]))
print(Solution.get_min_in_rotated([25, 30, 5, 10, 15, 20]))
print(Solution.get_min_in_rotated([11, 13, 15, 17]))
print(Solution.get_min_in_rotated([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.get_min_in_rotated([1, 2]))
print(Solution.get_min_in_rotated([2, 1]))
print(Solution.get_min_in_rotated([3, 3, 3, 3, 3]))
print(Solution.get_min_in_rotated([1, 2, 2, 3, 3, 3, 5]))
print(Solution.get_min_in_rotated([5, 5, 5, 5, 1, 2, 3, 3]))
