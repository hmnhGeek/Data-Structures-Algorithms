# Problem link - https://www.geeksforgeeks.org/merge-two-sorted-arrays/#using-merge-of-mergesort
# Solution - https://www.youtube.com/watch?v=n7uwj04E0I4


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


class PointerSolution:
    """
        Time complexity is O(n*log(n) + m*log(m)) and space complexity is O(1).
    """
    @staticmethod
    def merge(arr1, arr2):
        n, m = len(arr1), len(arr2)
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if arr1[i] > arr2[j]:
                temp = arr1[i]
                arr1[i] = arr2[j]
                arr2[j] = temp
                i -= 1
                j += 1
            else:
                break
        QuickSort.sort(arr1)
        QuickSort.sort(arr2)
        return arr1, arr2


class GapMethod:
    @staticmethod
    def _swap(arr1, i, arr2, j):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]

    @staticmethod
    def merge(arr1, arr2):
        """
            Time complexity is O({n + m} * log(n + m)) and space complexity is O(1).
        """
        n, m = len(arr1), len(arr2)
        length = n + m
        gap = (n + m)//2 + (n + m)%2
        while gap > 0:
            left = 0
            right = left + gap
            while right < length:
                if left < n and right < n:
                    # both are on a1 arr
                    GapMethod._swap(arr1, left, arr1, right)
                elif left < n and right >= n:
                    # left on a1 and right on a2
                    GapMethod._swap(arr1, left, arr2, right - n)
                else:
                    # both are on a2 arr
                    GapMethod._swap(arr2, left - n, arr2, right - n)
                left += 1
                right += 1
            if gap == 1:
                break
            gap = (gap//2) + (gap%2)
        return arr1, arr2


print(PointerSolution.merge([1, 3, 4, 5], [2, 4, 6, 8]))
print(PointerSolution.merge([5, 8, 9], [4, 7, 8]))
print(PointerSolution.merge([2, 4, 7, 10], [2, 3]))
print(PointerSolution.merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))
print(PointerSolution.merge([0, 1], [2, 3]))
print()
print(GapMethod.merge([1, 3, 4, 5], [2, 4, 6, 8]))
print(GapMethod.merge([5, 8, 9], [4, 7, 8]))
print(GapMethod.merge([2, 4, 7, 10], [2, 3]))
print(GapMethod.merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13]))
print(GapMethod.merge([0, 1], [2, 3]))
