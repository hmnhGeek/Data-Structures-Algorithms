class Solution:
    @staticmethod
    def get_first_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return low if low in range(len(arr)) else -1

    @staticmethod
    def get_last_occurrence(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
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
        return left, right


print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(Solution.get_occurrences([2, 4, 6, 8, 8, 8, 11, 13], 80))