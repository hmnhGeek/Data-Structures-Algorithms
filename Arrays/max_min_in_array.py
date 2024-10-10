# Problem link - https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/


class Utility:
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
    def _quick_sort(arr, low, high):
        if low < high:
            partition_index = Utility._get_partition_index(arr, low, high)
            Utility._quick_sort(arr, low, partition_index - 1)
            Utility._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def quick_sort(arr):
        n = len(arr)
        Utility._quick_sort(arr, 0, n - 1)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low)/2)
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
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
    def _merge_sort(arr, low, high):
        if low >= high:
            return

        mid = int(low + (high - low)/2)
        Utility._merge_sort(arr, low, mid)
        Utility._merge_sort(arr, mid + 1, high)
        merged = Utility._merge(arr, low, high)
        arr[low:high+1] = merged

    @staticmethod
    def merge_sort(arr):
        Utility._merge_sort(arr, 0, len(arr) - 1)


def get_min_max(arr):
    copy = [i for i in arr]
    # sort in O(nlog(n)) and get the min from 0th index and max from last index
    Utility.quick_sort(copy)
    return copy[0], copy[-1]


def get_min_max_merge_sort(arr):
    copy = [i for i in arr]
    # sort in O(nlog(n)) and get the min from 0th index and max from last index
    Utility.merge_sort(copy)
    return copy[0], copy[-1]


def get_min_max_linear_time(arr):
    # This will take O(n) time and O(1) space.

    _min = 1e6
    _max = -1e6

    for i in arr:
        if i < _min:
            _min = i
        if i > _max:
            _max = i

    return _min, _max


print(get_min_max([3, 5, 4, 1, 9]))
print(get_min_max([22, 14, 8, 17, 35, 3]))
print(get_min_max_merge_sort([3, 5, 4, 1, 9]))
print(get_min_max_merge_sort([22, 14, 8, 17, 35, 3]))
print(get_min_max_linear_time([3, 5, 4, 1, 9]))
print(get_min_max_linear_time([22, 14, 8, 17, 35, 3]))