# Problem link - https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# Solution - https://www.youtube.com/watch?v=n7uwj04E0I4


class QuickSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        QuickSort._sort(arr, 0, n - 1)

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
    def merge_without_extra_space(arr1, arr2):
        """
            Time complexity is O(n + m + nlog(n) + mlog(m)) and space complexity is O(1).
        """
        i, j = len(arr1) - 1, 0
        while i >= 0 and j < len(arr2):
            if arr1[i] > arr2[j]:
                temp = arr1[i]
                arr1[i] = arr2[j]
                arr2[j] = temp
            else:
                break
            i -= 1
            j += 1
        QuickSort.sort(arr1)
        QuickSort.sort(arr2)
        print(arr1, arr2)


Solution.merge_without_extra_space([2, 4, 7, 10], [2, 3])
Solution.merge_without_extra_space([1, 5, 9, 10, 15, 20], [2, 3, 8, 13])
Solution.merge_without_extra_space([0, 1], [2, 3])
