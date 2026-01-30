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

