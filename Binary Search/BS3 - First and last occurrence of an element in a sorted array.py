# Problem link - https://www.naukri.com/code360/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
# Solution - https://www.youtube.com/watch?v=hjR1IYVx9lY&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=4


class Solution:
    """
        Time complexity is O(2*log(n)) and space complexity is O(1).
    """

    @staticmethod
    def get_first_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return low if low in range(len(arr)) else -1

    @staticmethod
    def get_last_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return high if high in range(len(arr)) else -1

    @staticmethod
    def get_occurrences(arr, x):
        left, right = Solution.get_first_occurrence(arr, x), Solution.get_last_occurrence(arr, x)
        if left == -1 or right == -1:
            return -1, -1
        if arr[left] != x:
            return -1, -1
        return left, right


print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 80))
print(Solution.get_occurrences([0, 1, 1, 5], 1))
print(Solution.get_occurrences([0, 0, 1, 1, 2, 2, 2, 2], 2))
print(Solution.get_occurrences([1, 3, 3, 5], 2))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
print(Solution.get_occurrences([5, 7, 7, 8, 8, 10], 6))
print(Solution.get_occurrences([], 0))
