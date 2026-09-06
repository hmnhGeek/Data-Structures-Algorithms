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
        i, j = low, high
        pivot = arr[low]
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
    def merge_without_extra_space(a, b):
        i = len(a) - 1
        j = 0
        while i >= 0 and j < len(b):
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                break
        QuickSort.sort(a)
        QuickSort.sort(b)
        print(a, b)


Solution.merge_without_extra_space([2, 4, 7, 10], [2, 3])
Solution.merge_without_extra_space([1, 5, 9, 10, 15, 20], [2, 3, 8, 13])
Solution.merge_without_extra_space([0, 1], [2, 3])
