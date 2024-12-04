# Problem link - https://www.naukri.com/code360/problems/aggressive-cows_1082559
# Solution - https://www.youtube.com/watch?v=R_Mfw4ew-Vo&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=18


class QuickSort:
    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _sort(arr, low, high):
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._sort(arr, low, partition_index - 1)
            QuickSort._sort(arr, partition_index + 1, high)

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


class Solution:
    @staticmethod
    def _placing_all_cows_possible(arr, mid, k):
        """
            This will take O(n) time and O(1) space.
        """

        # assume first cow is placed at index 0.
        cows_placed = 1
        last_cow_index = 0

        # start placing rest of the cows from index 1.
        for i in range(1, len(arr)):
            # if the distance difference is larger than or equal to mid-distance, we can place the current cow at ith
            # index.
            if arr[i] - arr[last_cow_index] >= mid:
                # place the cow and update the last cow index.
                cows_placed += 1
                last_cow_index = i

        # if you were able to place more than equal to k cows, return True, else False.
        return cows_placed >= k

    @staticmethod
    def aggressive_cows(arr, k):
        """
            Overall time complexity is O(nlog(n)) and space complexity is O(1).
        """

        if k <= 0:
            return

        # This will take O(nlog(n)) time.
        QuickSort.sort(arr)

        # the max distance between any two cows can be when one is placed at beginning and the other at the end.
        low, high = 1, arr[-1] - arr[0]
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._placing_all_cows_possible(arr, mid, k)

            # if it is possible to place all the cows with `mid` minimum distance, then lets try for even higher minimum
            # distance.
            if is_possible:
                low = mid + 1
            else:
                # else we must lower the minimum distance.
                high = mid - 1

        # high points to the correct answer.
        return high


print(Solution.aggressive_cows([0, 3, 4, 7, 9, 10], 4))
print(Solution.aggressive_cows([1, 2, 3], 2))
print(Solution.aggressive_cows([4, 2, 1, 3, 6], 2))
print(Solution.aggressive_cows([1, 2, 4, 8, 9], 3))
print(Solution.aggressive_cows([10, 1, 2, 7, 5], 3))
