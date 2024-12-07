# Problem link - https://www.geeksforgeeks.org/problems/target-sum-1626326450/1
# Solution - https://www.youtube.com/watch?v=b3GD8263-PQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=22


def recursive():
    """
        T: O(2^n) and S: O(n)
    """

    def solve(arr, index, target):
        if target == 0:
            return 1
        if index == 0:
            return 1 if arr[0] == target else 0

        left = 0
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index])
        right = solve(arr, index - 1, target)
        return left + right

    def target_sum(arr, k):
        n = len(arr)
        return solve(arr, n - 1, k)

    print(target_sum([1, 2, 3, 1], 3))


def memoized():
    """
        T: O(n*k) and S: O(n + nk)
    """

    def solve(arr, index, target, dp):
        if target == 0:
            return 1
        if index == 0:
            return 1 if arr[0] == target else 0

        if dp[index][target] is not None:
            return dp[index][target]

        left = 0
        if arr[index] <= target:
            left = solve(arr, index - 1, target - arr[index], dp)
        right = solve(arr, index - 1, target, dp)
        dp[index][target] = left + right
        return dp[index][target]

    def target_sum(arr, k):
        n = len(arr)
        dp = {i: {j: None for j in range(k + 1)} for i in range(n)}
        return solve(arr, n - 1, k, dp)

    print(target_sum([1, 2, 3, 1], 3))


def tabulation():
    """
        T: O(n*k) and S: O(nk)
    """

    def target_sum(arr, k):
        n = len(arr)
        dp = {i: {j: 0 for j in range(k + 1)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = 1 if arr[0] == j else 0
        for i in dp:
            dp[i][0] = 1
        for index in range(1, n):
            for target in range(k + 1):
                left = 0
                if arr[index] <= target:
                    left = dp[index - 1][target - arr[index]]
                right = dp[index - 1][target]
                dp[index][target] = left + right
        return dp[n - 1][k]

    print(target_sum([1, 2, 3, 1], 3))


def space_optimized():
    """
        T: O(n*k) and S: O(k)
    """

    def target_sum(arr, k):
        n = len(arr)
        prev = {j: 0 for j in range(k + 1)}
        for j in prev:
            prev[j] = 1 if arr[0] == j else 0
        prev[0] = 1
        for index in range(1, n):
            curr = {j: 0 for j in range(k + 1)}
            curr[0] = 1
            for target in range(k + 1):
                left = 0
                if arr[index] <= target:
                    left = prev[target - arr[index]]
                right = prev[target]
                curr[target] = left + right
            prev = curr
        return prev[k]

    print(target_sum([1, 2, 3, 1], 3))


class Solution:
    @staticmethod
    def _subset_sum(arr, k):
        n = len(arr)
        prev = {j: 0 for j in range(k + 1)}
        for j in prev:
            prev[j] = 1 if arr[0] == j else 0
        prev[0] = 1
        for index in range(1, n):
            curr = {j: 0 for j in range(k + 1)}
            curr[0] = 1
            for target in range(k + 1):
                left = 0
                if arr[index] <= target:
                    left = prev[target - arr[index]]
                right = prev[target]
                curr[target] = left + right
            prev = curr
        return prev[k]

    @staticmethod
    def target_sum(arr, target):
        """
            Overall time complexity is O(n * target) and space complexity is O(target).
        """

        s = sum(arr)
        if (s + target) % 2 == 1:
            return 0
        k = (s + target) // 2
        return Solution._subset_sum(arr, k)


print(Solution.target_sum([1, 1, 1, 1, 1], 3))
print(Solution.target_sum([1, 2, 3, 1], 3))
print(Solution.target_sum([1, 2, 3], 2))
print(Solution.target_sum([1, 1], 0))
print(Solution.target_sum([1], 1))
