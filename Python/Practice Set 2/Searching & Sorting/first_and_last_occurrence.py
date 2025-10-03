# Problem link - https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1


class Solution:
    @staticmethod
    def get_first_occurrence(arr, x):
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def get_last_occurrence(arr, x):
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high

    @staticmethod
    def get_occurrences(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        n = len(arr)
        first = Solution.get_first_occurrence(arr, x)
        last = Solution.get_last_occurrence(arr, x)
        if 0 <= first < n and arr[first] == x and 0 <= last < n and arr[last] == x:
            return first, last
        return -1, -1


print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 7, 123, 125], 90))
