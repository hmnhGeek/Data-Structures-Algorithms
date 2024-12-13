class Solution:
    @staticmethod
    def search(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == x:
                return mid
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            if arr[mid] <= arr[high]:
                if arr[mid] <= x <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif arr[low] <= x <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution.search([3, 1, 2, 3, 3, 3, 3], 2))