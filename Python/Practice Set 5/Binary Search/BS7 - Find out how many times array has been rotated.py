class Solution:
    @staticmethod
    def get_min_in_rotated(arr):
        low = 0
        high = len(arr) - 1
        min_val = 1e6
        index = -1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] <= arr[mid]:
                if arr[low] < min_val:
                    min_val = arr[low]
                    index = low
                low = mid + 1
            else:
                if arr[mid] <= min_val:
                    min_val = arr[mid]
                    index = mid
                high = mid - 1
        return index


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
