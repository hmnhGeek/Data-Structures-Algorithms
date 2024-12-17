class Solution:
    @staticmethod
    def get_peak(arr):
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return arr[0]
        if arr[0] > arr[1]:
            return arr[0]
        if arr[-1] > arr[-2]:
            return arr[-1]
        low, high = 1, len(arr) - 2
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution.get_peak([1, 5, 1, 2, 1]))
print(Solution.get_peak([1, 8, 1, 5, 3]))
print(Solution.get_peak([1, 2, 1]))