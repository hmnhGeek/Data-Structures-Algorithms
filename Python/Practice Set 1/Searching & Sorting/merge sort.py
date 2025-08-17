class Solution:
    @staticmethod
    def sort(arr):
        low = 0
        high = len(arr) - 1
        Solution._sort(arr, low, high)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        Solution._sort(arr, low, mid)
        Solution._sort(arr, mid + 1, high)
        arr[low:high+1] = Solution._merge(arr, low, high)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low)/2)
        left, right = arr[low:mid+1], arr[mid+1:high+1]
        i, j = 0, 0
        merged = []

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

