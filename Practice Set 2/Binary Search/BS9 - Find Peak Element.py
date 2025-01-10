class Solution:
    @staticmethod
    def get_peak(arr):
        n = len(arr)
        if n == 0:
            return -1e6
        if n == 1:
            return arr[0]
        if arr[1] < arr[0]:
            return arr[0]
        if arr[-1] > arr[-2]:
            return arr[-1]
        low, high = 1, n - 2
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return arr[mid]
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution.get_peak([1, 5, 1, 2, 1]))
print(Solution.get_peak([1, 8, 1, 5, 3]))
print(Solution.get_peak([1, 2, 1]))
print(Solution.get_peak([1, 2, 3, 1]))
print(Solution.get_peak([1, 2, 1, 3, 5, 6, 4]))
print(Solution.get_peak([1, 2, 4, 5, 7, 8, 3]))
print(Solution.get_peak([10, 20, 15, 2, 23, 90, 80]))
print(Solution.get_peak([1, 2, 3]))
