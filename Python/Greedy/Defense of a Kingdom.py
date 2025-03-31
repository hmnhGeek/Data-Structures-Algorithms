# Problem link - https://www.spoj.com/problems/DEFKIN/
# Solution - https://www.youtube.com/watch?v=fk1yIirivEo


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
    def defense(n, m, mtx):
        xs, ys = [0,], [0, ]
        for i in range(len(mtx)):
            xs.append(mtx[i][0])
            ys.append(mtx[i][1])
        xs.append(n + 1)
        ys.append(m + 1)
        QuickSort.sort(xs)
        QuickSort.sort(ys)
        max_x, max_y = 0, 0
        for i in range(1, len(xs)):
            max_x = max(max_x, xs[i] - xs[i - 1] - 1)
            max_y = max(max_y, ys[i] - ys[i - 1] - 1)
        return max_x * max_y


print(Solution.defense(15, 8, [[3, 8], [11, 2], [8, 6]]))