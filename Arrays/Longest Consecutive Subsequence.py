class QuickSort:
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

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        return QuickSort._sort(arr, 0, len(arr) - 1)


class SortingSolution:
    @staticmethod
    def get_longest_consecutive_length(arr):
        copy = [i for i in arr]
        QuickSort.sort(copy)
        longest_length = 1
        sequence_length = 1
        last_value = copy[0]
        i = 1
        while i < len(copy):
            if copy[i] == copy[i - 1] + 1:
                sequence_length += 1
                last_value = copy[i]
                longest_length = max(longest_length, sequence_length)
            elif copy[i] != copy[i - 1]:
                sequence_length = 1
                last_value = arr[i]
            i += 1
        return longest_length


print(SortingSolution.get_longest_consecutive_length([2, 6, 1, 9, 4, 5, 3]))
print(SortingSolution.get_longest_consecutive_length([1, 9, 3, 10, 4, 20, 2]))
print(SortingSolution.get_longest_consecutive_length([15, 13, 12, 14, 11, 10, 9]))
