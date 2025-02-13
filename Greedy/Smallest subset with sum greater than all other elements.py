class QuickSort:
    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)

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
        arr[low], arr[j] = arr[j], arr[low]
        return j


class Solution:
    @staticmethod
    def solve(arr):
        QuickSort.sort(arr)
        total_sum = sum(arr)
        subset_sum = 0
        subset_length = 0
        i = len(arr) - 1
        while subset_sum <= total_sum:
            total_sum -= arr[i]
            subset_sum += arr[i]
            i -= 1
        return len(arr) - 1 - i


print(Solution.solve([3, 1, 7, 1]))
print(Solution.solve([1, 2, 1]))
