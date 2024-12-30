class QuickSort:
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
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        return QuickSort._sort(arr, 0, len(arr) - 1)


class SortingSolution:
    @staticmethod
    def get_longest_consecutive_length(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        # create a copy of the original array so that we don't modify the original array. This will take O(n) space.
        copy = [i for i in arr]

        # sort the copied array in O(n * log(n)) time.
        QuickSort.sort(copy)

        # create the longest length variable (this will be the final answer).
        longest_length = 1

        # for each sequence, find the length and then use it to update the longest length variable.
        sequence_length = 1

        # assume that the 0th index element is the first sequence that we start off with
        last_value = copy[0]
        # thus, start with index = 1
        i = 1

        # loop on the copied array in O(n) time.
        while i < len(copy):
            # if the current element is consecutive to the previous element
            if copy[i] == copy[i - 1] + 1:
                # increment the sequence length
                sequence_length += 1
                # update the last value to this element
                last_value = copy[i]
                # update the longest length
                longest_length = max(longest_length, sequence_length)

            # if however, the previous and current element is not consecutive
            elif copy[i] != copy[i - 1]:
                # break the sequence by resetting the sequence length to 1.
                sequence_length = 1
                # and update the last value
                last_value = arr[i]

            # increment i. Note that if the previous and current element are same, there's nothing to do.
            i += 1

        # return the longest length.
        return longest_length


class Solution:
    @staticmethod
    def get_longest_consecutive_length(arr):
        hash_set = dict.fromkeys(arr)
        longest_length = 1
        for i in hash_set:
            if i - 1 not in hash_set:
                count = 1
                element = i
                while element + 1 in hash_set:
                    count += 1
                    element += 1
                longest_length = max(longest_length, count)
        return longest_length


print(SortingSolution.get_longest_consecutive_length([2, 6, 1, 9, 4, 5, 3]))
print(SortingSolution.get_longest_consecutive_length([1, 9, 3, 10, 4, 20, 2]))
print(SortingSolution.get_longest_consecutive_length([15, 13, 12, 14, 11, 10, 9]))
print(SortingSolution.get_longest_consecutive_length([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]))
print(SortingSolution.get_longest_consecutive_length([100, 4, 200, 1, 3, 2]))
print(SortingSolution.get_longest_consecutive_length([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

print()

print(Solution.get_longest_consecutive_length([2, 6, 1, 9, 4, 5, 3]))
print(Solution.get_longest_consecutive_length([1, 9, 3, 10, 4, 20, 2]))
print(Solution.get_longest_consecutive_length([15, 13, 12, 14, 11, 10, 9]))
print(Solution.get_longest_consecutive_length([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]))
print(Solution.get_longest_consecutive_length([100, 4, 200, 1, 3, 2]))
print(Solution.get_longest_consecutive_length([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))