class MergeSort:
    @staticmethod
    def sort(arr):
        MergeSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low) / 2)
        left, right = arr[low:mid+1], arr[mid+1:high+1]
        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high+1] = MergeSort._merge(arr, low, high)


class Solution:
    @staticmethod
    def aggressive_cows(arr, k):
        if k <= 0:
            return
        n = len(arr)
        low, high = 0, max(arr) - min(arr)
