# Problem link - https://www.geeksforgeeks.org/problems/minimize-the-heights3351/1
# Solution - https://www.youtube.com/watch?v=30vDmZg5MZ8

class QuickSort:
    @staticmethod
    def sort(arr):
        low, high = 0, len(arr) - 1
        QuickSort._sort(arr, low, high)

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
    def minimize_the_heights(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """
        QuickSort.sort(arr)
        n = len(arr)
        smallest, largest = arr[0] + k, arr[-1] - k
        result = largest - smallest
        mini, maxi = 0, 0
        for i in range(n - 1):
            mini = min(smallest, arr[i + 1] - k)
            maxi = max(largest, arr[i] + k)
            if mini < 0:
                continue
            result = min(result, maxi - mini)
        return result


print(Solution.minimize_the_heights([5, 8, 10, 1], 2))
print(Solution.minimize_the_heights([3, 9, 12, 16, 20], 3))
