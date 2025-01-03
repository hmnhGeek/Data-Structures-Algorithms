# Problem link - https://www.naukri.com/code360/problems/search-in-rotated-sorted-array_1082554
# Solution - https://www.youtube.com/watch?v=5qGrJbHhqFs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=5


class Solution:
    @staticmethod
    def search(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define a search space
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)

            # if mid-element is x, return mid.
            if arr[mid] == x:
                return mid

            # if left part is sorted
            if arr[low] <= arr[mid]:
                # and x could be in the left part, then reduce high
                if arr[low] <= x <= arr[mid]:
                    high = mid - 1
                else:
                    # if x is in right part (unsorted), then increase low
                    low = mid + 1
            else:
                # if right part is sorted, and x is in this part, increment low
                if arr[mid] <= x <= arr[high]:
                    low = mid + 1
                else:
                    # else decrement high.
                    high = mid - 1
        # return -1 as element is not found.
        return -1


arr1 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
for i in arr1:
    print(Solution.search(arr1, i))
print(Solution.search(arr1, 100))
print(Solution.search([12, 15, 18, 2, 4], 2))
print(Solution.search([8, 9, 4, 5], 3))
print(Solution.search([2, 3, 5, 8], 3))
print(Solution.search([1, 2, 3, 4], 4))
