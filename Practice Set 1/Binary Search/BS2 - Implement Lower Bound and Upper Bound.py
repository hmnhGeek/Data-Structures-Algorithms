# Problem link - https://www.naukri.com/code360/problems/lower-bound_8165382
# Problem link - https://www.naukri.com/code360/problems/implement-upper-bound_8165383
# Solution - https://www.youtube.com/watch?v=6zhGS79oQ4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=3


class Solution:
    @staticmethod
    def get_lower_bound(arr, x):
        """
            Gives the smallest index i such that arr[i] >= x.

            Time complexity is O(log(n)) and space complexity is O(1).
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def get_upper_bound(arr, x):
        """
            Gives the smallest index i such that arr[i] > x.

            Time complexity is O(log(n)) and space complexity is O(1).
        """
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return low


print("Lower Bounds")
print(Solution.get_lower_bound([3, 5, 8, 15, 19], 10))
print(Solution.get_lower_bound([1, 2, 2, 3], 0))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 0))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 2))
print(Solution.get_lower_bound([1, 2, 2, 3, 3, 5], 7))
print()
print("Upper Bounds")
print(Solution.get_upper_bound([2, 4, 6, 7], 5))
print(Solution.get_upper_bound([1, 4, 7, 8, 10], 7))
print(Solution.get_upper_bound([1, 2, 5, 6, 10], 10))
print(Solution.get_upper_bound([1, 5, 5, 7, 7, 9, 10], 5))
