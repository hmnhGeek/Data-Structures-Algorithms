# Problem link - https://www.geeksforgeeks.org/problems/minimum-swaps/1
# Solution - https://www.youtube.com/watch?v=kFe_LRWuZjE


class QuickSort:
    @staticmethod
    def _get_partition_index(arr, low, high):
        pivot = arr[low][0]
        i, j = low, high
        while i < j:
            while arr[i][0] <= pivot and i <= high - 1:
                i += 1
            while arr[j][0] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)


class Solution:
    @staticmethod
    def find_min_swaps(arr):
        """
            Time complexity is O(nlog(n)) and space complexity is O(n).
        """

        n = len(arr)

        # construct n-sized temp array storing the element and its index in a tuple format from the original array. This
        # will take O(n) time and O(n) space.
        temp = [(arr[i], i) for i in range(n)]

        # sort the temp array based on the 0th element of each tuple, i.e., original elements, in O(n * log(n)) time.
        QuickSort.sort(temp)

        # store the swaps count.
        swaps_count = 0

        # iterate on the temp array now in O(n) time. This is used to build back the given array.
        i = 0
        while i < n:
            # until the ith index has its correct tuple where tuple's 1st value points to i, do the following.
            while temp[i][1] != i:
                # get the index with which we should swap
                idx = temp[i][1]
                # perform the swap
                temp[i], temp[idx] = temp[idx], temp[i]
                # increment the swap value
                swaps_count += 1
            # once the correct tuple is at i, move to next i.
            i += 1

        # return swaps count.
        return swaps_count


print(Solution.find_min_swaps([10, 19, 6, 3, 5]))
print(Solution.find_min_swaps([6, 3, 1, 2, 4, 5]))
print(Solution.find_min_swaps([1, 3, 4, 5, 6]))
print(Solution.find_min_swaps([2, 8, 5, 4]))
