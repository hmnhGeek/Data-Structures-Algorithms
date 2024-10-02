class QuickSort:
    def __init__(self):
        pass

    @classmethod
    def _divide_and_conquer(cls, arr, low, high):
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
            partition_index = cls._divide_and_conquer(arr, low, high)
            cls._quick_sort(arr, low, partition_index - 1)
            cls._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._quick_sort(arr, 0, len(arr) - 1)


arr1 = [4, 6, 2, 5, 7, 9, 1, 9, 3]
QuickSort.sort(arr1)
print(arr1)
