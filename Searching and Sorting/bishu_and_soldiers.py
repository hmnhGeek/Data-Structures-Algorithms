# Problem link - https://www.hackerearth.com/problem/algorithm/bishu-and-soldiers-227/
# Solution - https://www.youtube.com/watch?v=hT1sOIcenBA


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
    def _get_presum(arr):
        result = []
        _sum = 0
        for i in range(len(arr)):
            _sum += arr[i]
            result.append(_sum)
        return result

    @staticmethod
    def _get_less_equal_powers(arr, x, low, high):
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high

    @staticmethod
    def bishu_soldiers(powers, queries):
        """
            Overall time complexity is O({n + m} * log(n)) and space complexity is O(n + m).
        """

        # Takes O(n*log(n)) time to sort.
        QuickSort.sort(powers)
        # Takes O(n) time to compute and takes O(n) space.
        pre_sum = Solution._get_presum(powers)
        # Takes O(2m) space for m sized queries.
        result = []
        # Takes O(m*log(n)) time where m is the number of queries.
        for q in queries:
            powers_less_than_q = Solution._get_less_equal_powers(powers, q, 0, len(powers) - 1)
            result.append((powers[powers_less_than_q], pre_sum[powers_less_than_q]))
        return result


print(Solution.bishu_soldiers([1, 2, 3, 4, 5, 6, 7], [3, 10, 2]))
