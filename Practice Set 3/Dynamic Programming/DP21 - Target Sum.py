# Problem link - https://www.geeksforgeeks.org/problems/target-sum-1626326450/1
# Solution - https://www.youtube.com/watch?v=b3GD8263-PQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=22


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, j):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left + right

    def target_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(target_sum([1, 2, 3, 1], 3))


def memoized():
    """
        Time complexity is O(nk) and space complexity is O(n + nk).
    """
    def solve(arr, i, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 1 if arr[0] == j else 0
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if arr[i] <= j:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    def target_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(target_sum([1, 2, 3, 1], 3))


def tabulation():
    """
        Time complexity is O(nk) and space complexity is O(nk).
    """
    def target_sum(arr, target):
        n = len(arr)
        dp = {i: {j: 0 for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 1
        for j in dp[0]:
            if arr[0] == j:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left + right
        return dp[n - 1][target]

    print(target_sum([1, 2, 3, 1], 3))


def space_optimized():
    """
        Time complexity is O(nk) and space complexity is O(k).
    """
    def target_sum(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        for j in prev:
            if arr[0] == j:
                prev[j] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    print(target_sum([1, 2, 3, 1], 3))


class Solution:
    @staticmethod
    def _subset_sum(arr, target):
        n = len(arr)
        prev = {j: 0 for j in range(target + 1)}
        prev[0] = 1
        for j in prev:
            if arr[0] == j:
                prev[j] = 1
        for i in range(1, n):
            curr = {j: 0 for j in range(target + 1)}
            curr[0] = 1
            for j in range(target + 1):
                left = 0
                if arr[i] <= j:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left + right
            prev = curr
        return prev[target]

    @staticmethod
    def target_sum(arr, d):
        """
            Time complexity is O(n * (sum + d)) and space complexity is O(sum + d).
        """

        numerator = sum(arr) + d
        if numerator % 2 == 1:
            return -1
        target = numerator // 2
        return Solution._subset_sum(arr, target)


print(Solution.target_sum([1, 1, 1, 1, 1], 3))
print(Solution.target_sum([1, 2, 3, 1], 3))
print(Solution.target_sum([1, 2, 3], 2))
print(Solution.target_sum([1, 1], 0))
print(Solution.target_sum([1], 1))