# Problem link - https://leetcode.com/problems/partition-equal-subset-sum/description/
# Solution - https://www.youtube.com/watch?v=7win3dcgo3k&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=16


def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

    def solve(arr, i, j):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j
        left = False
        if j >= arr[i]:
            left = solve(arr, i - 1, j - arr[i])
        right = solve(arr, i - 1, j)
        return left or right

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def memoized():
    """
        Time complexity is O(n*k) and space complexity is O(n + nk).
    """
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

    def solve(arr, i, j, dp):
        if j == 0:
            return True
        if i == 0:
            return arr[0] == j
        if dp[i][j] is not None:
            return dp[i][j]
        left = False
        if j >= arr[i]:
            left = solve(arr, i - 1, j - arr[i], dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = left or right
        return dp[i][j]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def tabulation():
    """
        Time complexity is O(n*k) and space complexity is O(n*k).
    """
    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: False for j in range(target + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = True
        dp[0][arr[0]] = True
        for i in range(1, n):
            for j in range(target + 1):
                left = False
                if j >= arr[i]:
                    left = dp[i - 1][j - arr[i]]
                right = dp[i - 1][j]
                dp[i][j] = left or right
        return dp[n - 1][target]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


def space_optimized():
    """
        Time complexity is O(n*k) and space complexity is O(k).
    """
    def subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            curr[0] = True
            for j in range(target + 1):
                left = False
                if j >= arr[i]:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left or right
            prev = curr
        return prev[target]

    print(subset_sum([1, 2, 3, 4], 4))
    print(subset_sum([4, 3, 2, 1], 5))
    print(subset_sum([2, 5, 1, 6, 7], 4))
    print(subset_sum([6, 1, 2, 1], 4))
    print(subset_sum([1, 7, 2, 9, 10], 6))
    print(subset_sum([3, 34, 4, 12, 5, 2], 9))
    print(subset_sum([3, 34, 4, 12, 5, 2], 30))


class Solution:
    @staticmethod
    def subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            curr[0] = True
            for j in range(target + 1):
                left = False
                if j >= arr[i]:
                    left = prev[j - arr[i]]
                right = prev[j]
                curr[j] = left or right
            prev = curr
        return prev[target]

    @staticmethod
    def partition_equals_subset_sum(arr):
        """
            Time complexity is O(n * (n/2)) and space complexity is O(n/2).
        """
        k = sum(arr)
        if k % 2 != 0:
            return False
        target = k // 2
        return Solution.subset_sum(arr, target)


print(Solution.partition_equals_subset_sum([2, 3, 3, 3, 4, 5]))
print(Solution.partition_equals_subset_sum([3, 1, 1, 2, 2, 1]))
print(Solution.partition_equals_subset_sum([5, 6, 5, 11, 6]))
print(Solution.partition_equals_subset_sum([2, 2, 1, 1, 1, 1, 1, 3, 3]))
print(Solution.partition_equals_subset_sum([8, 7, 6, 12, 4, 5]))
print(Solution.partition_equals_subset_sum([1, 5, 11, 5]))
print(Solution.partition_equals_subset_sum([1, 3, 5]))
print(Solution.partition_equals_subset_sum([1, 2, 3, 5]))
