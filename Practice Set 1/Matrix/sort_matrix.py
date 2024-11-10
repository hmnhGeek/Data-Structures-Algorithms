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
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._sort(arr, low, partition_index - 1)
            QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)


class Solution:
    @staticmethod
    def sort_matrix(mtx):
        n, m = len(mtx), len(mtx[0])
        temp = []
        for i in range(n):
            for j in range(m):
                temp.append(mtx[i][j])
        QuickSort.sort(temp)
        result = []
        i = 0
        while i < n * m:
            row = [temp[j] for j in range(i, i + m)]
            i += m
            result.append(row)
        return result


print(
    Solution.sort_matrix(
        [
            [10, 20, 30, 40],
            [15, 25, 35, 45],
            [27, 29, 37, 48],
            [32, 33, 39, 50]
        ]
    )
)

print(
    Solution.sort_matrix(
        [
            [1, 5, 3], [2, 8, 7], [4, 6, 9]
        ]
    )
)
