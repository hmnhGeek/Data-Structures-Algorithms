class QuickSort:
    @staticmethod
    def sort(arr):
        return QuickSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
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


class Solution:
    @staticmethod
    def solve(arr):
        QuickSort.sort(arr)
        temp = []
        i, j = 0, len(arr) - 1
        while i <= j:
            if i == j:
                temp.append(arr[i])
            else:
                temp.append(arr[i])
                temp.append(arr[j])
            i += 1
            j -= 1
        _sum = 0
        for i in range(len(temp) - 1):
            _sum += abs(temp[i + 1] - temp[i])
        _sum += abs(temp[0] - temp[-1])
        return _sum


print(Solution.solve([1, 2, 4, 8]))
print(Solution.solve([1, 2, 8, 3]))
print(Solution.solve([1, 2, 3, 4, 5]))
print(Solution.solve([3, 4, 2, 9, 1, 5]))
print(Solution.solve([1, 3]))
