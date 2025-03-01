# Problem link - https://leetcode.com/problems/partition-array-for-maximum-sum/description/
# Solution - https://www.youtube.com/watch?v=PhWWJmaKfMc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=55


def recursive():
    """
        Time complexity is exponential and space complexity is O(n^2).
    """

    def solve(arr, i, n, k):
        if i == n:
            return 0
        max_item = -1e6
        max_cost = -1e6
        for j in range(i, min(n, i + k)):
            max_item = max(max_item, arr[j])
            length = j - i + 1
            cost = (length * max_item) + solve(arr, j + 1, n, k)
            max_cost = max(max_cost, cost)
        return max_cost

    def partition(arr, k):
        n = len(arr)
        return solve(arr, 0, n, k)

    print(partition([1, 15, 7, 9, 2, 5, 10], 3))
    print(partition([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
    print(partition([1], 1))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n^2 + n).
    """

    def solve(arr, i, n, k, dp):
        if i == n:
            return 0
        if dp[i]:
            return dp[i]
        max_item = -1e6
        max_cost = -1e6
        for j in range(i, min(n, i + k)):
            max_item = max(max_item, arr[j])
            length = j - i + 1
            cost = (length * max_item) + solve(arr, j + 1, n, k, dp)
            max_cost = max(max_cost, cost)
        dp[i] = max_cost
        return dp[i]

    def partition(arr, k):
        n = len(arr)
        dp = {i: None for i in range(n + 1)}
        return solve(arr, 0, n, k, dp)

    print(partition([1, 15, 7, 9, 2, 5, 10], 3))
    print(partition([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
    print(partition([1], 1))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def partition(arr, k):
        n = len(arr)
        dp = {i: -1e6 for i in range(n + 1)}
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            max_item = -1e6
            max_cost = -1e6
            for j in range(i, min(n, i + k)):
                max_item = max(max_item, arr[j])
                length = j - i + 1
                cost = (length * max_item) + dp[j + 1]
                max_cost = max(max_cost, cost)
            dp[i] = max_cost
        return dp[0]

    print(partition([1, 15, 7, 9, 2, 5, 10], 3))
    print(partition([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
    print(partition([1], 1))


recursive()
print()
memoized()
print()
tabulation()
