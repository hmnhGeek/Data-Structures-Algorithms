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
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)


class Solution:
    @staticmethod
    def is_present(arr, target):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        # Sort the array in O(n * log(n)) time
        QuickSort.sort(arr)
        n = len(arr)

        # loop in the array till last 3rd element
        for i in range(n - 2):
            # initiate j and k
            j, k = i + 1, n - 1
            while j < k:
                _sum = arr[i] + arr[j] + arr[k]
                if _sum == target:
                    return True

                # if sum > target, we must decrease from right side
                if _sum > target:
                    k -= 1
                else:
                    # else increase from left side.
                    j += 1
        return False


print(Solution.is_present([1, 4, 45, 6, 10, 8], 13))
print(Solution.is_present([1, 2, 4, 3, 6, 7], 10))
print(Solution.is_present([40, 20, 10, 3, 6, 7], 24))
