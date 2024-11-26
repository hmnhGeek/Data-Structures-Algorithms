class Solution:
    @staticmethod
    def find_peak_element(arr):
        if len(arr) == 1:
            return arr[0]
        if arr[0] >= arr[1]:
            return arr[0]
        if arr[-1] >= arr[-2]:
            return arr[-1]
        low, high = 1, len(arr) - 2
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            if arr[mid] > arr[mid - 1] and arr[mid] == arr[mid + 1]:
                return arr[mid]
            if arr[mid] > arr[mid + 1] and arr[mid] == arr[mid - 1]:
                return arr[mid]

            if arr[mid - 1] < arr[mid]:
                low = mid + 1
            elif arr[mid] > arr[mid + 1]:
                high = mid - 1
            elif arr[mid - 1] == arr[mid] == arr[mid + 1]:
                low = mid + 1
            elif arr[mid + 1] > arr[mid]:
                low = mid + 1
            elif arr[mid - 1] > arr[mid]:
                high = mid - 1
            elif arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]:
                low = mid + 1
        return -1


print(Solution.find_peak_element([3, 3, 3, 3]))
print(Solution.find_peak_element([1, 2, 3, 1]))
print(Solution.find_peak_element([1, 2, 1, 3, 5, 6, 4]))
print(Solution.find_peak_element([1, 8, 1, 5, 3]))
print(Solution.find_peak_element([1, 2, 1]))
print(Solution.find_peak_element([5, 10, 20, 15]))
print(Solution.find_peak_element([10, 20, 15, 2, 23, 90, 90]))
print(Solution.find_peak_element([1, 1, 1]))
print(Solution.find_peak_element([1, 2, 3, 4, 5]))
print(Solution.find_peak_element([5, 4, 3, 2, 1]))
