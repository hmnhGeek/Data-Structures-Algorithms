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


def get_min_max(arr):
    copy = [i for i in arr]
    # sort in O(nlog(n)) and get the min from 0th index and max from last index
    Utility.quick_sort(copy)
    return copy[0], copy[-1]


print(get_min_max([3, 5, 4, 1, 9]))
print(get_min_max([22, 14, 8, 17, 35, 3]))