class Solution:
    @staticmethod
    def distribute(arr, m):
        """
            Time complexity is O(n * log(n)) and space complexity is O(1).
        """

        arr.sort()
        i, j = 0, m - 1
        diff = 1e6
        while j < len(arr):
            diff = min(diff, arr[j] - arr[i])
            j += 1
            i += 1
        return diff


print(Solution.distribute([3, 4, 1, 9, 56, 7, 9, 12], 5))
print(Solution.distribute([7, 3, 2, 4, 9, 12, 56], 3))
print(Solution.distribute([3, 4, 1, 9, 56], 5))
