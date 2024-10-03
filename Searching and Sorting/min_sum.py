class QuickSort:
    @classmethod
    def _get_partition_index(cls, arr, low, high):
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

    @classmethod
    def _quick_sort(cls, arr, low, high):
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._quick_sort(arr, low, partition_index - 1)
            QuickSort._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        n = len(arr)
        return QuickSort._quick_sort(arr, 0, n - 1)
