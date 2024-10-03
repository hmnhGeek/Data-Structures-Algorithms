# Problem link - https://www.geeksforgeeks.org/problems/minimum-sum4058/1


class QuickSort:
    """
        Refer to explanation in file quick_sort.py for this algorithm.
    """
    @classmethod
    def _get_partition_index(cls, arr, low, high):
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

    @classmethod
    def _quick_sort(cls, arr, low, high):
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._quick_sort(arr, low, partition_index - 1)
            QuickSort._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        n = len(arr)
        return QuickSort._quick_sort(arr, 0, n - 1)


class Solution:
    @staticmethod
    def get_min_sum(arr):
        copy = [i for i in arr]
        QuickSort.sort(copy)
        num1, num2 = 0, 0
        multiplier = 1
        for i in range(-1, -len(copy) - 1, -2):
            num1 += copy[i]*multiplier
            if i - 1 >= -len(copy):
                num2 += copy[i - 1]*multiplier
            multiplier *= 10
        return num1 + num2


print(Solution.get_min_sum([6, 8, 4, 5, 2, 3]))
print(Solution.get_min_sum([5, 3, 0, 7, 4]))