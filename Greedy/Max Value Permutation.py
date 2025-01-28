# Problem link - https://www.geeksforgeeks.org/problems/maximize-arrii-of-an-array0026/1


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
    def get_max_value_permutation(arr):
        QuickSort.sort(arr)
        val = 0
        for i in range(len(arr)):
            val += arr[i] * i
        return val


print(Solution.get_max_value_permutation([5, 3, 2, 4, 1]))
print(Solution.get_max_value_permutation([1, 2, 3]))
print(Solution.get_max_value_permutation([7, 7, 7, 7]))
