class Solution:
    @staticmethod
    def get_rotation_index(arr):
        low, high = 0, len(arr) - 1
        ans, index = 1e6, -1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] == arr[mid] == arr[high]:
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = low
                low += 1
                high -= 1
                continue
            if arr[low] <= arr[mid]:
                if ans > arr[low]:
                    ans = arr[low]
                    index = low
                low += 1
            else:
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = mid
                high -= 1
        return index


print(Solution.get_rotation_index([3, 4, 5, 1, 2]))
print(Solution.get_rotation_index([1, 2, 4, 5, 7]))
print(Solution.get_rotation_index([3, 3, 3, 3, 2, 3, 3]))
print(Solution.get_rotation_index([1, 2, 3]))
print(Solution.get_rotation_index([2, 3, 4, 1]))
