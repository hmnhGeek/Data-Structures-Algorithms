# Problem link - https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1


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
    def get_kth_smallest(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """

        if k <= 0 or k > len(arr):
            return -1
        QuickSort.sort(arr)
        return arr[k - 1]


print(Solution.get_kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(Solution.get_kth_smallest([2, 3, 1, 20, 15], 4))
