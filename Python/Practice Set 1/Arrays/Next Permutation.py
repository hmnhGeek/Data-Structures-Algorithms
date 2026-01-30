class Utility:
    @staticmethod
    def sort(arr, i):
        Utility._sort(arr, i, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = Utility._get_partition_index(arr, low, high)
        Utility._sort(arr, low, partition_index - 1)
        Utility._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

class Solution:
    @staticmethod
    def get_next_permutation(arr):
        n = len(arr)
        breakpoint_index = Solution._get_breakpoint_index(arr, n)
        if breakpoint_index < 0:
            return arr[-1:-n-1:-1]
        just_greater_element_index = Solution._get_just_greater(arr, breakpoint_index, n)
        arr[breakpoint_index], arr[just_greater_element_index] = arr[just_greater_element_index], arr[breakpoint_index]
        Utility.sort(arr, breakpoint_index + 1)
        return arr

    @staticmethod
    def _get_breakpoint_index(arr, n):
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                return i
        return -1

    @staticmethod
    def _get_just_greater(arr, breakpoint_index, n):
        element = arr[breakpoint_index]
        for i in range(n - 1, breakpoint_index, -1):
            if arr[i] > element:
                return i
        return -1
