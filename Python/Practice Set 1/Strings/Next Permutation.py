class Solution:
    @staticmethod
    def get_breakpoint_index(arr):
        n = len(arr)
        for i in range(n - 1, 0, -1):
            if arr[i - 1] < arr[i]:
                return i - 1
        return -1

    @staticmethod
    def reverse_part(arr, index):
        n = len(arr)
        i, j = index + 1, n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

