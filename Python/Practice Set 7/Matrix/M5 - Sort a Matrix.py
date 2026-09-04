class MergeSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        MergeSort._sort(arr, 0, n - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high+1] = MergeSort._merge(arr, low, high)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low)/2)
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
        i, j = 0, 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


class Solution:
    @staticmethod
    def sort_matrix(mtx):
        n, m = len(mtx), len(mtx[0])
        flattened_mtx = Solution._flatten(mtx, n, m)
        MergeSort.sort(flattened_mtx)
        return Solution._reconstruct(flattened_mtx, n, m)

    @staticmethod
    def _flatten(mtx, n, m):
        flattened = []
        for i in range(n):
            for j in range(m):
                flattened.append(mtx[i][j])
        return flattened

    @staticmethod
    def _reconstruct(flattened, n, m):
        mtx = []
        i = 0
        while i < n:
            j = 0
            row = []
            while j < m:
                row.append(flattened[(i * m) + j])
                j += 1
            i += 1
            mtx.append(row)
        return mtx


print(Solution.sort_matrix(
    [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]
))

print(Solution.sort_matrix([[1, 5, 3], [2, 8, 7], [4, 6, 9]]))
