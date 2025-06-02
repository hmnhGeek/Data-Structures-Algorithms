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
        i, j = low, high
        pivot = arr[low]
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Solution:
    @staticmethod
    def sort_matrix(mtx):
        """
            Time complexity is O(nm * log(nm)) and space complexity is O(nm).
        """
        n, m = len(mtx), len(mtx[0])
        arr = Solution._flatten(mtx, n, m)
        QuickSort.sort(arr)
        Solution._build_back(mtx, arr, n, m)
        for i in range(n):
            print(mtx[i])
        print()

    @staticmethod
    def _flatten(mtx, n, m):
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(mtx[i][j])
        return arr

    @staticmethod
    def _build_back(mtx, arr, n, m):
        counter = 0
        for i in range(n):
            for j in range(m):
                mtx[i][j] = arr[counter]
                counter += 1


Solution.sort_matrix(
    [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]
)

Solution.sort_matrix(
    [
        [1, 5, 3], [2, 8, 7], [4, 6, 9]
    ]
)

Solution.sort_matrix(
    [
        [5, 4, 7],
        [1, 3, 8],
        [2, 9, 6]
    ]
)

Solution.sort_matrix(
    [
        [5, 4, 7],
        [1, 3, 8]
    ]
)