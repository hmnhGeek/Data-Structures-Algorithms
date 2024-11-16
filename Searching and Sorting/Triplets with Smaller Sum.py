# Problem link - https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1
# Solution - https://www.youtube.com/watch?v=9455buJlb_k


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
        arr[j], arr[low] = arr[low], arr[j]
        return j

    @staticmethod
    def _sort(arr, low, high):
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._sort(arr, low, partition_index - 1)
            QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)


class Solution:
    @staticmethod
    def triplet_sum_smaller_than(arr, target):
        """
            Overall time complexity is O(n^2) and space complexity is O(1).
        """

        # This will take O(n*log(n)) time.
        QuickSort.sort(arr)
        n = len(arr)
        count = 0

        # This will run for n times. We need not run till n - 2 because the inner while loop will take care of
        # index out of bounds.
        for i in range(n):
            # place j next to `i`.
            j = i + 1
            # place k at last index.
            k = n - 1
            # This loop will run for additional n times.
            while j < k:
                # if the sum < target, then all the elements between j and k (k included and j excluded) will have
                # sum < target because the arr is sorted. Hence, increment the count with (k - j). Also, remain at
                # same `k` index, i.e., do not reset it to n - 1. Why? Because now we have incremented j by +1. So,
                # if previous `j` was, say, giving sum >= target for k = n - 1, then increasing `j` will definitely
                # do that too. Thus, we can avoid these iterations.
                if arr[i] + arr[j] + arr[k] < target:
                    count += (k - j)
                    j += 1
                else:
                    # if the sum >= target, reduce k.
                    k -= 1

        # finally return the count.
        return count


print(Solution.triplet_sum_smaller_than([-2, 0, 1, 3], 2))
print(Solution.triplet_sum_smaller_than([5, 1, 3, 4, 7], 12))