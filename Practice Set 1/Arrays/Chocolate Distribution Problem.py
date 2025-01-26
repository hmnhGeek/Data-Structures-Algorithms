# Problem link - https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
# Solution - https://www.youtube.com/watch?v=oYNU1TD9W5Y


class MergeSort:
    @staticmethod
    def sort(arr):
        MergeSort._sort(arr, 0, len(arr) - 1)

    @staticmethod
    def _merge(arr, low, high):
        mid = int(low + (high - low) / 2)
        left, right = arr[low:mid + 1], arr[mid + 1:high + 1]
        i, j = 0, 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    @staticmethod
    def _sort(arr, low, high):
        if low >= high:
            return
        mid = int(low + (high - low) / 2)
        MergeSort._sort(arr, low, mid)
        MergeSort._sort(arr, mid + 1, high)
        arr[low:high + 1] = MergeSort._merge(arr, low, high)


class Solution:
    @staticmethod
    def chocolate_distribution(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """

        # sort the array in O(n * log(n)) time.
        MergeSort.sort(arr)

        diff = 1e6
        n = len(arr)

        # loop on the windows
        for i in range(n - k + 1):
            up = arr[i + k - 1]
            low = arr[i]
            # update the difference
            diff = min(diff, up - low)

        # return the minimum difference
        return diff


print(Solution.chocolate_distribution([3, 4, 1, 9, 56, 7, 9, 12], 5))
print(Solution.chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 3))
print(Solution.chocolate_distribution([3, 4, 1, 9, 56], 5))
print(Solution.chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 5))
print(Solution.chocolate_distribution([6, 8, 11, 21, 90, 49], 4))
