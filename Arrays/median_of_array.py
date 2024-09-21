class MergeSort:
    def __init__(self):
        pass

    def merge(self, arr, low, high):
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

    def _sort(self, arr, low, high):
        if low >= high:
            return

        mid = int(low + (high - low)/2)
        self._sort(arr, low, mid)
        self._sort(arr, mid + 1, high)
        arr[low:high+1] = self.merge(arr, low, high)

    def sort(self, arr):
        self._sort(arr, 0, len(arr) - 1)

