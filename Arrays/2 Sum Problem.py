# Problem link - https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/
# Solution - https://www.youtube.com/watch?v=UXDSeD9mN-k&t=439s


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
        if low <= high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._sort(arr, low, partition_index - 1)
            QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)


class Solution:
    @staticmethod
    def two_sum(arr, target):
        """
            Time complexity is O(nlog(n)) and space complexity is O(1).
        """

        # O(nlog(n)) to sort the array
        QuickSort.sort(arr)

        # use left and right pointer to find the pairs.
        left = 0
        right = len(arr) - 1

        # store the result array.
        result = []

        # even if left ==  right, we want a pair, and hence left < right.
        while left < right:
            _sum = arr[left] + arr[right]
            # if the sum is equivalent to target
            if _sum == target:
                # append the pair and reduce the range.
                result.append((arr[left], arr[right]))
                left += 1
                right -= 1
            elif _sum > target:
                # if sum is larger, reduce from right
                right -= 1
            else:
                # else reduce from left
                left += 1
        # return the result
        return result


print(Solution.two_sum([-1, 0, 1, 2, -1, -4], 0))
print(Solution.two_sum([6, 1, 8, 0, 4, -9, -1, -10, -6, -5], 0))
print(Solution.two_sum([2, 7, 11, 15], 9))
print(Solution.two_sum([3, 2, 4], 6))
print(Solution.two_sum([3, 3], 6))
print(Solution.two_sum([0, -1, 2, -3, 1], -2))
print(Solution.two_sum([1, -2, 1, 0, 5], 0))
