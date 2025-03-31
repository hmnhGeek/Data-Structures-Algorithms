# Video - https://www.youtube.com/watch?v=WIrA4YexLRQ&t=49s


class QuickSort:
    def __init__(self):
        pass

    @classmethod
    def _divide_and_conquer(cls, arr, low, high):
        # take the first element, i.e., arr[low] as pivot. A pivot element can be any element from the
        # array, but we are taking the first element always. A pivot element is just a random element
        # which needs to be positioned correctly in the sorted array.
        pivot = arr[low]
        # create `i` and `j` variables at the low and high end of the array.
        i, j = low, high

        # unless i and j cross each other...
        while i < j:
            # find the first index between low and high which is greater than pivot. Note that to avoid
            # overflowing on the right side, we check `i` till high - 1 as we are already incrementing it
            # in the while loop.
            while arr[i] <= pivot and i <= high - 1:
                i += 1

            # find the first index between low and high which is smaller than or equal to the pivot.
            # Note that to avoid overflowing on the left side, we check `j` till low + 1 as we are
            # already decrementing it in the while loop.
            while arr[j] > pivot and j >= low + 1:
                j -= 1

            # check if `i < j` still, because if it is not, then there is no point in swapping `i` and `j`.
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # finally, we have segregated all the elements lower than pivot on one side and all the elements
        # greater than pivot on the right side. Now just swap the `low` index with `j` index so that
        # pivot comes to its correct position.
        arr[low], arr[j] = arr[j], arr[low]

        # return `j` which is the correct position of the pivot in the sorted array. Note that the array might
        # not be completely sorted yet, but it is confirmed that pivot is at its correct place in the sorted
        # array. This index is also called the partition index.
        return j

    @classmethod
    def _quick_sort(cls, arr, low, high):
        # if there are more than 1 element to sort, then only apply quick sort because a single element
        # is always sorted.
        if low < high:
            # the class method `_divide_and_conquer` takes a pivot in arr[low:high+1] and partitions the
            # array and places the pivot element at its correct position. Finally, it also returns the
            # partition index which is the index at which the pivot finally resides.
            partition_index = cls._divide_and_conquer(arr, low, high)

            # recursively sort the left and right part of the array.
            cls._quick_sort(arr, low, partition_index - 1)
            cls._quick_sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        """
            Since it is a divide and conquer technique, the time complexity is O(nlog(n)) and space complexity
            is O(1) as we are not using any extra space like in merge sort.
        """
        # pass the array to sort with low = 0 and high = n - 1.
        QuickSort._quick_sort(arr, 0, len(arr) - 1)


arr1 = [4, 6, 2, 5, 7, 9, 1, 9, 3]
QuickSort.sort(arr1)
print(arr1)
