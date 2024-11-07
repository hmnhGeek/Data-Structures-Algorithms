# Problem link - https://www.naukri.com/code360/problems/divisible-set_3754960?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=gDuZwBW9VvM&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=45


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
        if low < high:
            partition_index = QuickSort._get_partition_index(arr, low, high)
            QuickSort._sort(arr, low, partition_index - 1)
            QuickSort._sort(arr, partition_index + 1, high)

    @staticmethod
    def sort(arr):
        QuickSort._sort(arr, 0, len(arr) - 1)


class Solution:
    @staticmethod
    def get_longest_divisible_subset(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        # takes O(n) space
        copy = [i for i in arr]

        # takes O(n*log(n)) time
        QuickSort.sort(copy)

        # O(n) space.
        dp = {i: 1 for i in range(len(copy))}
        parents = {i: i for i in range(len(copy))}

        # O(n^2) time.
        for index in range(len(copy)):
            for prev in range(index):
                if copy[index] % copy[prev] == 0:
                    if dp[index] < 1 + dp[prev]:
                        dp[index] = 1 + dp[prev]
                        parents[index] = prev

        last_index_of_lis = max(dp, key=dp.get)
        result = []
        start_node = last_index_of_lis
        while parents[start_node] != start_node:
            result.append(copy[start_node])
            start_node = parents[start_node]
        result.append(copy[start_node])
        return result


print(Solution.get_longest_divisible_subset([1, 16, 7, 8, 4]))
print(Solution.get_longest_divisible_subset([1, 2, 5]))
print(Solution.get_longest_divisible_subset([3, 3, 3]))
print(Solution.get_longest_divisible_subset([1, 2, 4, 8]))
print(Solution.get_longest_divisible_subset([2, 4, 3, 8]))
print(Solution.get_longest_divisible_subset([10, 5, 3, 15, 20]))
print(Solution.get_longest_divisible_subset([18, 1, 3, 6, 13, 17]))
