# Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/description/


class Solution:
    @staticmethod
    def search(arr, target):
        """
            Time complexity is O(log(n)) and space is O(1).
        """
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == target:
                return mid
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
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
print(Solution.search([3, 3, 1, 3, 3, 3, 3], 1))
