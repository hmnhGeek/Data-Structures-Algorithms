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
        arr[j], arr[low] = arr[low], arr[j]
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


class Solution:
    @staticmethod
    def triplet_sum_smaller_than(arr, target):
        QuickSort.sort(arr)
        n = len(arr)
        count = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] < target:
                    count += (k - j)
                    j += 1
                else:
                    k -= 1
        return count


print(Solution.triplet_sum_smaller_than([-2, 0, 1, 3], 2))
print(Solution.triplet_sum_smaller_than([5, 1, 3, 4, 7], 12))