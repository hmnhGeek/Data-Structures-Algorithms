# Problem link - https://www.naukri.com/code360/problems/search-in-rotated-sorted-array_1082554
# Solution - https://www.youtube.com/watch?v=5qGrJbHhqFs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=5


class Solution:
    @staticmethod
    def search_in_rotated_sorted_array(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # define the search space.
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            # if the mid-element is equal to x, return the mid-index.
            if arr[mid] == x:
                return mid
            # if right part is sorted
            if arr[mid] <= arr[high]:
                # and x lies in right part
                if arr[mid] <= x <= arr[high]:
                    # increment low
                    low = mid + 1
                else:
                    # else, x must be in unsorted part
                    high = mid - 1
            # if left part is sorted and x is in left part
            elif arr[low] <= x <= arr[mid]:
                # move to the left half
                high = mid - 1
            else:
                # move to the right half
                low = mid + 1
        # if element is not found, return -1.
        return -1


arr1 = [7, 8, 9, 1, 2, 3, 4, 5, 6]
for i in arr1:
    print(Solution.search_in_rotated_sorted_array(arr1, i))
print(Solution.search_in_rotated_sorted_array(arr1, 100))
print(Solution.search_in_rotated_sorted_array([12, 15, 18, 2, 4], 2))
print(Solution.search_in_rotated_sorted_array([8, 9, 4, 5], 3))
print(Solution.search_in_rotated_sorted_array([2, 3, 5, 8], 3))
print(Solution.search_in_rotated_sorted_array([1, 2, 3, 4], 4))
