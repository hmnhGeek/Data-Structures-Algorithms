class Solution:
    def _merge(self, arr, low, high):
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

    def _merge_sort(self, arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low)/2)
        self._merge_sort(arr, low, mid)
        self._merge_sort(arr, mid + 1, high)
        arr[low:high+1] = self._merge(arr, low, high)

    def merge_sort(self, arr):
        self._merge_sort(arr, 0, len(arr) - 1)


arr1 = [2, 3, 4, 1]
Solution().merge_sort(arr1)
print(arr1)

arr2 = [56, 2, 45]
Solution().merge_sort(arr2)
print(arr2)

arr3 = [5, 6, 3, 2, 1, 6, 7]
Solution().merge_sort(arr3)
print(arr3)