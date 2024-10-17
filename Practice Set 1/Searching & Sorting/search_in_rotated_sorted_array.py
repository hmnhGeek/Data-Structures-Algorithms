# Problem link - https://leetcode.com/problems/search-in-rotated-sorted-array/description/


class Solution:
    @staticmethod
    def search(arr, target):
        """
            Time complexity is O(log(n)) and space is O(1).
        """

        low, high = 0, len(arr) - 1

        # Typical binary search while condition
        while low <= high:
            mid = int(low + (high - low) / 2)

            # if the target is found at mid, return mid.
            if arr[mid] == target:
                return mid

            # if sorted part cannot be identified because all three pointers are same, increment low and decrement
            # high and continue until you can identify sorted part.
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue

            # if the left part is sorted
            if arr[low] <= arr[mid]:
                # check if target lies in left part, if yes, move high
                if arr[low] <= target <= arr[mid]:
                    high = mid - 1
                else:
                    # else move low.
                    low = mid + 1
            # if right part is sorted
            else:
                # and the target is in right part, move low.
                if arr[mid] <= target <= arr[high]:
                    low = mid + 1
                else:
                    # else move high.
                    high = mid - 1

        # if the target is not found, return -1.
        return -1


print(Solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution.search([1], 0))
print(Solution.search([2, 5, -3, 0], 5))
print(Solution.search([2, 5, -3, 0], 1))
print(Solution.search([3, 3, 1, 3, 3, 3, 3], 1))
