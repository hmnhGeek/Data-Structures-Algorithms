# Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
# Solution - https://www.youtube.com/watch?v=hjR1IYVx9lY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=4


class Solution:
    @staticmethod
    def first_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        return low if low in range(len(arr)) else -1

    @staticmethod
    def last_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return high if high in range(len(arr)) else -1

    @staticmethod
    def get_occurrence(arr, x):
        # This will take O(2*log(n)) time and O(1) space.
        first, last = Solution.first_occurrence(arr, x), Solution.last_occurrence(arr, x)
        if arr[first] == x and arr[last] == x:
            return first, last
        return -1, -1


print(Solution.get_occurrence([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(Solution.get_occurrence([0, 1, 1, 5], 1))
print(Solution.get_occurrence([0, 0, 1, 1, 2, 2, 2, 2], 2))
print(Solution.get_occurrence([1, 3, 3, 5], 2))
