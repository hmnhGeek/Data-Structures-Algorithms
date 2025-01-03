# Problem link - https://www.geeksforgeeks.org/problems/sorted-matrix2333/1


class MergeSort:
    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low) / 2)
        left, right = arr[low:mid + 1], arr[mid + 1:high + 1]
        merged = []
        i, j = 0, 0
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

    @staticmethod
    def sort(arr):
        MergeSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low) / 2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high + 1] = MergeSort._merge(arr, low, high)


class Solution:
    @staticmethod
    def _flatten(mtx, n):
        arr = []
        for i in range(n):
            for j in range(n):
                arr.append(mtx[i][j])
        return arr

    @staticmethod
    def _repopulate(mtx, arr, n):
        for i in range(n):
            for j in range(n):
                mtx[i][j] = arr[i * n + j]

    @staticmethod
    def sort_mtx(mtx):
        """
            Overall time complexity is O(n^2 log(n)) and space complexity is O(n^2).
        """

        n = len(mtx)
        # This will take O(n^2) time and O(n^2) space.
        flattened_arr = Solution._flatten(mtx, n)
        # This will take O(n^2 * log(n)) time.
        MergeSort.sort(flattened_arr)
        # This will take another O(n^2) time.
        Solution._repopulate(mtx, flattened_arr, n)
        # Print the sorted matrix
        for i in range(n):
            print(mtx[i])


Solution.sort_mtx(
    [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]
)

Solution.sort_mtx([[1, 5, 3], [2, 8, 7], [4, 6, 9]])
