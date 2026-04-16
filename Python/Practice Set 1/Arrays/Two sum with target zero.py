# Problem link - https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1


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
    def two_sum(arr):
        """
            Time complexity is O(n * log(n)) time and space complexity is O(1).
        """

        # This will take O(n * log(n)) time.
        QuickSort.sort(arr)
        i = 0
        j = len(arr) - 1
        result = []
        while i < j:
            _sum = arr[i] + arr[j]
            if _sum == 0:
                result.append((arr[i], arr[j]))
                i += 1
                j -= 1
            elif _sum > 0:
                j -= 1
            else:
                i += 1
        return result


print(Solution.two_sum([-1, 0, 1, 2, -1, -4]))
print(Solution.two_sum([6, 1, 8, 0, 4, -9, -1, -10, -6, -5]))
