# Problem link and solution - https://www.youtube.com/watch?v=6zhGS79oQ4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=3

"""
    All these operations will take O(log(n)) time and O(1) space.
"""


class Solution:
    @staticmethod
    def get_lower_bound(arr, x):
        """
            Finds the index of the element which is >= x.
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return low if 0 <= low < len(arr) else -1

    @staticmethod
    def get_upper_bound(arr, x):
        """
            Returns the lowest index from array whose element > x.
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return low if 0 <= low < len(arr) else -1

    @staticmethod
    def get_insert_index(arr, x):
        return Solution.get_lower_bound(arr, x)

    @staticmethod
    def floor(arr, x):
        """
            Returns index where element <= x.
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return high if 0 <= high < len(arr) else -1


print(Solution.get_lower_bound([3, 5, 8, 15, 19], 5))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 8))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 9))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 800))
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 2))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 0))
print(Solution.get_upper_bound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 11))
print(Solution.get_upper_bound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 6))
print(Solution.get_upper_bound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 12))
print(Solution.floor([3, 5, 8, 15, 19], 10))