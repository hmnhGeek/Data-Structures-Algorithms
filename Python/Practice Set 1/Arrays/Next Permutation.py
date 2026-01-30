class Solution:
    @staticmethod
    def get_next_permutation(arr):
        n = len(arr)
        breakpoint_index = Solution._get_breakpoint_index(arr, n)
        if breakpoint_index < 0:
            return arr[-1:-n-1:-1]
        just_greater_element_index = Solution._get_just_greater(arr, breakpoint_index, n)
        arr[breakpoint_index], arr[just_greater_element_index] = arr[just_greater_element_index], arr[breakpoint_index]
        Utility._sort(arr, breakpoint_index + 1)
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