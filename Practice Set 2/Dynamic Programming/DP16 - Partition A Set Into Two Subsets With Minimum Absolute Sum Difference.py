def recursive():
    def solve(arr, i, j):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j

        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


def memoized():
    def solve(arr, i, j, dp):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j

        if dp[i][j] is not None:
            return dp[i][j]

        left = False
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left or right
        return dp[i][j]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


def tabulation():
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: False for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = True
        dp[0][arr[0]] = True
        for i in range(1, n):
            for j in range(target + 1):
                left = False
                if arr[i] <= j:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left or right
        return dp[n - 1][target]

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


def space_optimized():
    def subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            for j in range(target + 1):
                left = False
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left or right
            prev = curr
        return prev[target]

    print(subset_sum([1, 2, 3, 4], 9))
    print(subset_sum([1, 2, 3, 4], 5))


class Solution:
    @staticmethod
    def _subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            for j in range(target + 1):
                left = False
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left or right
            prev = curr
        return prev[target]

    @staticmethod
    def min_diff_subset(arr):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        _sum = sum(arr)
        if _sum % 2 == 0 and Solution._subset_sum(arr, _sum // 2):
            return 0
        min_dff = 1e6
        for s1 in range((_sum // 2) + 2):
            if Solution._subset_sum(arr, s1):
                min_dff = min(min_dff, abs(2*s1 - _sum))
        return min_dff


print(Solution.min_diff_subset([1, 2, 3, 4]))
print(Solution.min_diff_subset([3, 1, 5, 2, 8]))
print(Solution.min_diff_subset([8, 6, 5]))
print(Solution.min_diff_subset([3, 9, 7, 3]))
print(Solution.min_diff_subset([1, 6, 11, 5]))
print(Solution.min_diff_subset([1, 5, 11, 5]))
