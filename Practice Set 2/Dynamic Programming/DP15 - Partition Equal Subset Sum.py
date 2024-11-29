# Problem link - https://leetcode.com/problems/partition-equal-subset-sum/description/
# Solution - https://www.youtube.com/watch?v=7win3dcgo3k&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=16


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """

    def solve(arr, index, k):
        if k == 0:
            return True
        if index == 0:
            return arr[index] == k

        left = False
        if arr[index] <= k:
            left = solve(arr, index - 1, k - arr[index])
        right = solve(arr, index - 1, k)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    print(subset_sum([2, 3, 3, 3, 4, 5], 10))


def memoized():
    """
        Time complexity is O(n * k) and space complexity is O(n + nk).
    """

    def solve(arr, index, k, dp):
        if k == 0:
            return True
        if index == 0:
            return arr[index] == k

        if dp[index][k] is not None:
            return dp[index][k]

        left = False
        if arr[index] <= k:
            left = solve(arr, index - 1, k - arr[index], dp)
        right = solve(arr, index - 1, k, dp)
        dp[index][k] = left or right
        return dp[index][k]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    print(subset_sum([2, 3, 3, 3, 4, 5], 10))


def tabulation():
    """
        Time complexity is O(n * k) and space complexity is O(n * k).
    """

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: False for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = True
        dp[0][arr[0]] = True
        for index in range(1, n):
            for k in range(target + 1):
                left = False
                if arr[index] <= k:
                    left = dp[index - 1][k - arr[index]]
                right = dp[index - 1][k]
                dp[index][k] = left or right
        return dp[n - 1][target]

    print(subset_sum([2, 3, 3, 3, 4, 5], 10))


def space_optimized():
    """
        Time complexity is O(n * k) and space complexity is O(k).
    """

    def subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for index in range(1, n):
            curr = {j: False for j in range(target + 1)}
            for k in range(target + 1):
                left = False
                if arr[index] <= k:
                    left = prev[k - arr[index]]
                right = prev[k]
                curr[k] = left or right
            prev = curr
        return prev[target]

    print(subset_sum([2, 3, 3, 3, 4, 5], 10))


class Solution:
    @staticmethod
    def _subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for index in range(1, n):
            curr = {j: False for j in range(target + 1)}
            for k in range(target + 1):
                left = False
                if arr[index] <= k:
                    left = prev[k - arr[index]]
                right = prev[k]
                curr[k] = left or right
            prev = curr
        return prev[target]

    @staticmethod
    def partition_equals_subset_sum(arr):
        """
            Time complexity is O(n * sum(arr)) and space complexity is O(sum(arr)).
        """
        _sum = sum(arr)
        if _sum % 2 == 1:
            return False
        target = _sum // 2
        return Solution._subset_sum(arr, target)


print(Solution.partition_equals_subset_sum([2, 3, 3, 3, 4, 5]))
print(Solution.partition_equals_subset_sum([3, 1, 1, 2, 2, 1]))
print(Solution.partition_equals_subset_sum([5, 6, 5, 11, 6]))
print(Solution.partition_equals_subset_sum([2, 2, 1, 1, 1, 1, 1, 3, 3]))
print(Solution.partition_equals_subset_sum([8, 7, 6, 12, 4, 5]))
print(Solution.partition_equals_subset_sum([1, 5, 11, 5]))
print(Solution.partition_equals_subset_sum([1, 3, 5]))
print(Solution.partition_equals_subset_sum([1, 2, 3, 5]))
