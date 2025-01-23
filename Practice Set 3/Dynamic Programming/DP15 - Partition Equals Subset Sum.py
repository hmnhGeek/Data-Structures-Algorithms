def recursive():
    """
        Time complexity is O(2^n) and space complexity is O(n).
    """
    def solve(arr, i, k):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k
        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i])
        right = solve(arr, i - 1, k)
        return left or right

    def subset_sum(arr, target):
        n = len(arr)
        return solve(arr, n - 1, target)

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
    def solve(arr, i, k, dp):
        if k == 0:
            return True
        if i == 0:
            return arr[0] == k
        if dp[i][k] is not None:
            return dp[i][k]
        left = False
        if arr[i] <= k:
            left = solve(arr, i - 1, k - arr[i], dp)
        right = solve(arr, i - 1, k, dp)
        dp[i][k] = left or right
        return dp[i][k]

    def subset_sum(arr, target):
        n = len(arr)
        dp = {i: {j: None for j in range(target + 1)} for i in range(n)}
        return solve(arr, n - 1, target, dp)

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
            for k in range(target + 1):
                left = False
                if arr[i] <= k:
                    left = dp[i - 1][k - arr[i]]
                right = dp[i - 1][k]
                dp[i][k] = left or right
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
            for k in range(target + 1):
                left = False
                if arr[i] <= k:
                    left = prev[k - arr[i]]
                right = prev[k]
                curr[k] = left or right
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
    def _subset_sum(arr, target):
        n = len(arr)
        prev = {j: False for j in range(target + 1)}
        prev[0] = True
        prev[arr[0]] = True
        for i in range(1, n):
            curr = {j: False for j in range(target + 1)}
            curr[0] = True
            for k in range(target + 1):
                left = False
                if arr[i] <= k:
                    left = prev[k - arr[i]]
                right = prev[k]
                curr[k] = left or right
            prev = curr
        return prev[target]

    @staticmethod
    def partition_equals_subset_sum(arr):
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
