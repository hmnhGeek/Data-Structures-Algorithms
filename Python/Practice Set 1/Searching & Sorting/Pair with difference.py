# Problem link - https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1
# Solution - https://www.youtube.com/watch?v=5IUyc7cPD9E


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
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Solution:
    @staticmethod
    def pair_with_difference(arr, diff):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """
        QuickSort.sort(arr)
        for i in arr:
            if Solution._find(arr, i + diff):
                return i, i + diff
        return -1

    @staticmethod
    def _find(arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == x:
                return True
            if arr[mid] > x:
                high = mid - 1
            else:
                low = mid + 1
        return False


print(Solution.pair_with_difference([5, 20, 3, 2, 5, 80], 78))
print(Solution.pair_with_difference([90, 70, 20, 80, 50], 45))
print(Solution.pair_with_difference([1], 1))
