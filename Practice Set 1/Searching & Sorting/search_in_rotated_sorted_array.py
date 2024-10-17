class Solution:
    @staticmethod
    def search(arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid

            if arr[low] <= arr[mid]:
                if arr[low] <= target <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] <= target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


print(Solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution.search([1], 0))
print(Solution.search([2, 5, -3, 0], 5))
print(Solution.search([2, 5, -3, 0], 1))
