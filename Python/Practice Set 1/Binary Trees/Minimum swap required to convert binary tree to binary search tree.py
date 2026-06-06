class QuickSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        QuickSort._sort(arr, 0, n - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

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
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Util:
    @staticmethod
    def _swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def min_swaps_to_sort(arr):
        n = len(arr)
        helper_arr = [(arr[i], i) for i in range(n)]
        QuickSort.sort(helper_arr)
        count_swaps = 0
        for i in range(n):
            if helper_arr[i][1] != i:
                Util._swap(helper_arr, i, helper_arr[i][1])
                count_swaps += 1
                i -= 1
        return count_swaps

