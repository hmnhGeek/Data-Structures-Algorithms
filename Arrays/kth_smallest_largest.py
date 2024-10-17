class Sorting:
    @staticmethod
    def _partition(arr, low, high):
        i, j = low, high
        pivot = arr[low]

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
    def _quick_sort(arr, low, high):
        if low >= high:
            return
        partition_index = Sorting._partition(arr, low, high)
        Sorting._quick_sort(arr, low, partition_index - 1)
        Sorting._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def quick_sort(arr):
        return Sorting._quick_sort(arr, 0, len(arr) - 1)


class MergeSort:
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

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return

        mid = int(low + (high - low)/2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high+1] = MergeSort._merge(arr, low, high)

    @staticmethod
    def sort(arr):
        n = len(arr)
        MergeSort._sort(arr, 0, n - 1)


def get_kth_smallest(arr, k):
    """
        Time complexity is O(nlog(n)) and space complexity is O(n).
    """

    # create a copy of the array so that the input array is not modified.
    # it will take O(n) space.
    copy = [i for i in arr]
    # sort the copied array in O(n*log(n)) time.
    Sorting.quick_sort(copy)
    # return the answer in O(1) time.
    return copy[k - 1] if 0 <= k - 1 < len(copy) else None


def get_kth_largest(arr, k):
    """
        Time complexity is O(nlog(n)) and space complexity is O(n).
    """

    # create a copy of the array so that the input array is not modified.
    # it will take O(n) space.
    copy = [i for i in arr]
    # sort the copied array in O(n*log(n)) time.
    MergeSort.sort(copy)
    # return the answer in O(1) time.
    return copy[len(copy) - k] if 0 <= len(copy) - k < len(copy) else None


print(get_kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(get_kth_smallest([2, 3, 1, 20, 15], 4))
print(get_kth_largest([7, 10, 4, 3, 20, 15], 3))
print(get_kth_largest([2, 3, 1, 20, 15], 4))