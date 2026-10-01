# Problem link - https://www.naukri.com/code360/problems/printing-longest-increasing-subsequence_8360670
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43


class Solution:
    @staticmethod
    def print_lis(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        n = len(arr)
        dp = {i: 1 for i in range(n)}
        parent = {i: i for i in range(n)}
        for i in range(n):
            for prev in range(i):
                if arr[i] > arr[prev] and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    parent[i] = prev
        lis_index = max(dp, key=dp.get)
        start_index = lis_index
        lis = []
        while parent[start_index] != start_index:
            lis.append(arr[start_index])
            start_index = parent[start_index]
        lis.append(arr[start_index])
        return lis[-1:-len(lis)-1:-1]


print(Solution.print_lis([5, 4, 11, 1, 16, 8]))
print(Solution.print_lis([1, 2, 2]))
print(Solution.print_lis([10, 20, 3, 40]))
print(Solution.print_lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(Solution.print_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(Solution.print_lis([1]))
print(Solution.print_lis([5, 6, 3, 4, 7, 6]))
print(Solution.print_lis([1, 2, 3, 4, 5]))
