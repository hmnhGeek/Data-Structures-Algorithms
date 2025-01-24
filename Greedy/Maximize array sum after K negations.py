# Problem link - https://www.geeksforgeeks.org/problems/maximize-sum-after-k-negations1149/1
# Solution - https://www.youtube.com/watch?v=8GDHYgbxTN4


class MergeSort:
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
    def sort(arr):
        MergeSort._sort(arr, 0, len(arr) - 1)

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
    def get_min(arr):
        min_index = -1
        min_elem = 1e6
        for i in range(len(arr)):
            if arr[i] < min_elem:
                min_elem = arr[i]
                min_index = i
        return min_index

    @staticmethod
    def maximize_sum(arr, k):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """

        # sort the array in O(n * log(n)) time and O(n) space.
        MergeSort.sort(arr)

        # loop in the array
        for i in range(len(arr)):
            # if the element is negative and we still can perform flip operations, then perform.
            if arr[i] < 0 and k > 0:
                arr[i] = -arr[i]
                k -= 1

        # get the minimum element index. In case k is still > 0, we can continuously flip the least element in order to
        # not affect the sum much.
        min_index = Solution.get_min(arr)

        # while k > 0, continuously flip min-elem.
        while k > 0:
            arr[min_index] = -arr[min_index]
            k -= 1

        # return the max sum obtained.
        return sum(arr)


print(Solution.maximize_sum([1, 2, -3, 4, 5], 1))
print(Solution.maximize_sum([5, -2, 5, -4, 5, -12, 5, 5, 5, 20], 5))
print(Solution.maximize_sum([4, 2, 3], 1))
print(Solution.maximize_sum([3, -1, 0, 2], 3))
print(Solution.maximize_sum([2, -3, -1, 5, -4], 2))
print(Solution.maximize_sum([9, 8, 8, 5], 4))
