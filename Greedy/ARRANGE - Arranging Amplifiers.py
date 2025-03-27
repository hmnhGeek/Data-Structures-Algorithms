class QuickSort:
    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def _get_partition_index(arr, low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            if arr[i] <= pivot and i <= high - 1:
                i += 1
            if arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j


class Solution:
    @staticmethod
    def arrange(arr):
        ones = 0
        n = len(arr)

        # count the number of ones as ones need to be placed in front regardless.
        for i in range(n):
            if arr[i] == 1:
                ones += 1

        # sort the array in descending order in O(n * log(n)) time.
        QuickSort.sort(arr)
        arr.reverse()

        # in the result place all the ones at front.
        result = [1]*ones

        # if there are only two elements remaining and they are 3 and 2, place them as 2 and 3.
        if n - ones == 2 and arr[0] == 3 and arr[1] == 2:
            result.append(2)
            result.append(3)
        else:
            # else place everything other than 1s in descending order.
            for i in range(n - ones):
                result.append(arr[i])
        return result


print(Solution.arrange([5, 6, 4]))
print(Solution.arrange([2, 3]))
