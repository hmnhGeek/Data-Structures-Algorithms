# Problem link - https://www.geeksforgeeks.org/problems/find-the-median0527/1


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


def find_median(arr):
    """
        Overall time complexity is O(nlog(n)) and space complexity is O(n).
    """

    # instead of modifying the original array, create a deep copy. This will take O(n) space.
    copied_arr = [i for i in arr]

    # apply merge sort on the copied array. This will take O(nlog(n)) time and O(n) space internally.
    merge_sort = MergeSort()
    merge_sort.sort(copied_arr)
    n = len(arr)

    # if the length of the array is even, return the avg of two middle elements.
    if n % 2 == 0:
        i = n // 2
        j = i - 1
        return (copied_arr[i] + copied_arr[j])/2

    # else return the middle element itself.
    return copied_arr[n//2]


print(find_median([90, 100, 78, 89, 67]))
print(find_median([56, 67, 30, 79]))
print(find_median([1, 3, 4, 2, 6, 5, 8, 7]))
print(find_median([4]*5))
