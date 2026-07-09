class Solution:
    @staticmethod
    def _first_occurrence(arr, x):
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] >= x:
                high = mid - 1
            else:
                low = mid + 1
        return low if low in range(n) else None

    @staticmethod
    def _last_occurrence(arr, x):
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high if high in range(n) else None

    @staticmethod
    def get_occurrences(arr, x):
        first = Solution._first_occurrence(arr, x)
        last = Solution._last_occurrence(arr, x)
        if first is not None and arr[first] != x:
            first = None
        if last is not None and arr[last] != x:
            last = None
        return first, last


print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 80))
print(Solution.get_occurrences([0, 1, 1, 5], 1))
print(Solution.get_occurrences([0, 0, 1, 1, 2, 2, 2, 2], 2))
print(Solution.get_occurrences([1, 3, 3, 5], 2))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))
print(Solution.get_occurrences([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))
print(Solution.get_occurrences([5, 7, 7, 8, 8, 10], 6))
print(Solution.get_occurrences([], 0))