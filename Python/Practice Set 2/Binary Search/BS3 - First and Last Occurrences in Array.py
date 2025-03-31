# Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
# Solution - https://www.youtube.com/watch?v=hjR1IYVx9lY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=4


class Solution:
    @staticmethod
    def get_first_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        if low not in range(len(arr)):
            return -1
        if arr[low] == x:
            return low
        return -1

    @staticmethod
    def get_last_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        if high not in range(len(arr)):
            return -1
        if arr[high] == x:
            return high
        return -1

    @staticmethod
    def get_occurrences(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        return Solution.get_first_occurrence(arr, x), Solution.get_last_occurrence(arr, x)



print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 80))
print(Solution.get_occurrences([0, 1, 1, 5], 1))
print(Solution.get_occurrences([0, 0, 1, 1, 2, 2, 2, 2], 2))
print(Solution.get_occurrences([1, 3, 3, 5], 2))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
print(Solution.get_occurrences([5, 7, 7, 8, 8, 10], 6))
print(Solution.get_occurrences([], 0))
