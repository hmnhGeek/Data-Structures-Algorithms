# Problem link - https://www.geeksforgeeks.org/problems/find-the-median0527/1


class QuickSort:
    @staticmethod
    def sort(arr):
        return QuickSort._sort(arr, 0, len(arr) - 1)

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
    def get_median(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """
        QuickSort.sort(arr)
        n = len(arr)
        if n % 2 == 1:
            return arr[(n - 1)//2]
        return (arr[n//2] + arr[n//2 - 1])/2


print(Solution.get_median([90, 100, 78, 89, 67]))
print(Solution.get_median([56, 67, 30, 79]))
print(Solution.get_median([1, 2]))
