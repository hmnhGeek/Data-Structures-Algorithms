# Problem link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1


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
    def sort_matrix(mtx):
        """
            Time complexity is O(n^2 * log(n)) and space complexity is O(n^2).
        """
        n = len(mtx)
        flattened = []
        for i in range(n):
            for j in range(n):
                flattened.append(mtx[i][j])
        QuickSort.sort(flattened)
        sorted_matrix = []
        row_idx = 0
        while row_idx < n:
            row = []
            for i in range(n):
                row.append(flattened[n * row_idx + i])
            sorted_matrix.append(row)
            row_idx += 1
        return sorted_matrix


print(Solution.sort_matrix(
    [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]
))

print(Solution.sort_matrix([[1, 5, 3], [2, 8, 7], [4, 6, 9]]))
