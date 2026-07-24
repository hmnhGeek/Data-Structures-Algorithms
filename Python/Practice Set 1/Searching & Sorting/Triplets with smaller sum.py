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
        arr[j], arr[low] = arr[low], arr[j]
        return j


class Solution:
    @staticmethod
    def triplets_with_smaller_sum(arr, target):
        QuickSort.sort(arr)
        n = len(arr)
        result = []
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                _sum = arr[i] + arr[j] + arr[k]
                if _sum < target:
                    result.append((arr[i], arr[j], arr[k]))
                    for p in range(k - 1, j, -1):
                        result.append((arr[i], arr[j], arr[p]))
                    j += 1
                else:
                    k -= 1
        return result


print(Solution.triplets_with_smaller_sum([-2, 0, 1, 3], 2))
print(Solution.triplets_with_smaller_sum([5, 1, 3, 4, 7], 12))
