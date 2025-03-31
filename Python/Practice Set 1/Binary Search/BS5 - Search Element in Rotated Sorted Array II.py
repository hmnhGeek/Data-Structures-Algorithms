# Problem link - https://www.naukri.com/code360/problems/search-in-a-rotated-sorted-array-ii_7449547
# Solution - https://www.youtube.com/watch?v=w2G2W8l__pc&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=6


class Solution:
    @staticmethod
    def search(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define search space
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            # return mid if x is found.
            if arr[mid] == x:
                return mid
            # if all three indices point to the same value, it is impossible to find the sorted/unsorted parts, hence,
            # shrink the search space and continue.
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            # if right part is sorted
            if arr[mid] <= arr[high]:
                # and x could be in right part
                if arr[mid] <= x <= arr[high]:
                    # search in right part
                    low = mid + 1
                else:
                    # else, search in left part
                    high = mid - 1
            # if left part is sorted and x could be in left part
            elif arr[low] <= x <= arr[mid]:
                # search in left part
                high = mid - 1
            else:
                # else, search in right part
                low = mid + 1
        # return -1, if element is not found
        return -1


print(Solution.search([3, 1, 2, 3, 3, 3, 3], 2))
print(Solution.search([6, 10, 1, 3, 5], 3))
print(Solution.search([3, 4, 5, 0, 0, 1, 2], 4))
print(Solution.search([31, 44, 56, 0, 10, 13], 47))
print(Solution.search([2, 5, 6, 0, 0, 1, 2], 0))
print(Solution.search([2, 5, 6, 0, 0, 1, 2], 3))
print(Solution.search([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 3))
print(Solution.search([7, 8, 1, 2, 3, 3, 3, 4, 5, 6], 10))
