# Problem link - https://www.naukri.com/code360/problems/search-in-rotated-sorted-array_1082554
# Solution - https://www.youtube.com/watch?v=5qGrJbHhqFs&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=5


class Solution:
    @staticmethod
    def search_in_rotated_sorted(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        # typical binary search starting points
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)

            # if element is found, return the index.
            if arr[mid] == x:
                return mid

            # now check if the right part is linearly increasing or not.
            if arr[mid] < arr[high]:
                # if it is and the target element falls in the right part only, then...
                if arr[mid] < x <= arr[high]:
                    # increment low.
                    low = mid + 1
                else:
                    # else the element could be in the left part.
                    high = mid - 1
            else:
                # check if x falls in left part or not.
                if arr[low] <= x < arr[mid]:
                    # if it does, decrement high.
                    high = mid - 1
                else:
                    # else the element could be in the right part.
                    low = mid + 1
        # return -1 as the element was not found.
        return -1


def test(arr):
    for i in arr:
        print(f"{i} found at index = {Solution.search_in_rotated_sorted(arr, i)}")
    print(f"{100} found at index = {Solution.search_in_rotated_sorted(arr, 100)}")
    print()


test([7, 8, 9, 1, 2, 3, 4, 5, 6])
test([12, 15, 18, 2, 4])
test([8, 9, 4, 5])
test([2, 3, 5, 8])
test([])
test([10])