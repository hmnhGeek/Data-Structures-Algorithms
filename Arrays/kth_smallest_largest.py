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


print(get_kth_smallest([7, 10, 4, 3, 20, 15], 3))
print(get_kth_smallest([2, 3, 1, 20, 15], 4))