# Problem link - https://www.geeksforgeeks.org/problems/minimum-sum4058/1


class QuickSort:
    """
        Refer to explanation in file quick_sort.py for this algorithm.
    """
    @classmethod
    def _get_partition_index(cls, arr, low, high):
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

    @classmethod
    def _quick_sort(cls, arr, low, high):
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._quick_sort(arr, low, partition_index - 1)
            QuickSort._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        n = len(arr)
        return QuickSort._quick_sort(arr, 0, n - 1)


class Solution:
    """
        Overall time complexity is O(n*log(n)) and space complexity is O(n).
    """
    @staticmethod
    def get_min_sum(arr):
        # create a copy of the original array so that we don't modify the original array.
        # This will take O(n) space.
        copy = [i for i in arr]

        # apply quick sort on the copied array in O(n*log(n)) time. Sorting will ensure that the most significant
        # digits of each number is low.
        QuickSort.sort(copy)

        # create the two numbers and a multiplier for 10s powers.
        num1, num2 = 0, 0
        multiplier = 1

        # start iterating from the end of the copied array.
        for i in range(-1, -len(copy) - 1, -2):
            # assign digits to num1 and num2
            num1 += copy[i]*multiplier
            if i - 1 >= -len(copy):
                num2 += copy[i - 1]*multiplier
            # update the multiplier to the next power of 10.
            multiplier *= 10

        # return the sum of the numbers.
        return num1 + num2


print(Solution.get_min_sum([6, 8, 4, 5, 2, 3]))
print(Solution.get_min_sum([5, 3, 0, 7, 4]))