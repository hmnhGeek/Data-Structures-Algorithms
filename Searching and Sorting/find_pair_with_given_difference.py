# Problem link - https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1


from typing import List


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


class BinarySearch:
    @staticmethod
    def search(arr: List[int], low: int, high: int, item: int) -> bool:
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == item:
                return True
            if arr[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        return False


class Solution:
    @staticmethod
    def find_pair(arr: List[int], x: int) -> bool:
        """
            Overall time complexity is O(n*log(n)) and space complexity is O(1).
        """
        # Takes O(n*log(n))
        QuickSort.sort(arr)
        # This will run for n times.
        for i in range(len(arr)):
            # Binary search will take O(log(n)) time.
            if BinarySearch.search(arr, 0, len(arr) - 1, abs(x - arr[i])):
                return True
        return False


print(Solution.find_pair([5, 20, 3, 2, 5, 80], 78))
print(Solution.find_pair([90, 70, 20, 80, 50], 45))
print(Solution.find_pair([1], 1))
print(Solution.find_pair([-10, 20], 30))