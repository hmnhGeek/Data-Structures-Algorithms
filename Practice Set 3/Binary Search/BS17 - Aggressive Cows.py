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
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        partition_index = QuickSort._get_partition_index(arr, low, high)
        QuickSort._sort(arr, low, partition_index - 1)
        QuickSort._sort(arr, partition_index + 1, high)


class Solution:
    @staticmethod
    def _num_placed(arr, mid):
        cows_placed = 1
        last_placed_at_index = 0
        for i in range(1, len(arr)):
            if arr[i] - arr[last_placed_at_index] >= mid:
                cows_placed += 1
                last_placed_at_index = i
        return cows_placed

    @staticmethod
    def aggressive_cows(arr, k):
        if k <= 0:
            return -1

        # sort the array in O(n * log(n)) time.
        QuickSort.sort(arr)

        # place all cows together at minimum and max distance of max(arr) at maximum.
        low, high = 0, arr[-1]
        while low <= high:
            mid = int(low + (high - low)/2)

            # get the number of cows placed in O(n) time.
            cows_placed = Solution._num_placed(arr, mid)

            # if less cows were placed, we must decrease the max distance between the cows
            if cows_placed < k:
                high = mid - 1

            # else we must increase the max distance
            else:
                low = mid + 1

        # return high which represents the max distance at which all k cows can be placed.
        return high


print(Solution.aggressive_cows([0, 3, 4, 7, 9, 10], 4))
print(Solution.aggressive_cows([1, 2, 3], 2))
print(Solution.aggressive_cows([4, 2, 1, 3, 6], 2))
print(Solution.aggressive_cows([1, 2, 4, 8, 9], 3))
print(Solution.aggressive_cows([10, 1, 2, 7, 5], 3))
print(Solution.aggressive_cows([2, 12, 11, 3, 26, 7], 5))
print(Solution.aggressive_cows([6, 7,  9, 11, 13, 15], 4))
