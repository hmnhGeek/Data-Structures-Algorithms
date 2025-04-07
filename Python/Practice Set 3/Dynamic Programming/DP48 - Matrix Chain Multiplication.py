# Problem link - https://www.naukri.com/code360/problems/matrix-chain-multiplication_975344?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=vRVfmbCFW7Y&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=49


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, i, j):
        if i == j:
            return 0
        min_cost = 1e6
        for k in range(i, j):
            cost = arr[i - 1] * arr[k] * arr[j] + solve(arr, i, k) + solve(arr, k + 1, j)
            min_cost = min(cost, min_cost)
        return min_cost

    def mcm(arr):
        n = len(arr)
        return solve(arr, 1, n - 1)

    print(mcm([10, 20, 30, 40, 50]))
    print(mcm([10, 20, 30, 40]))
    print(mcm([4, 5, 3, 2]))
    print(mcm([10, 15, 20, 25]))
    print(mcm([1, 4, 3, 2]))
    print(mcm([2, 1, 3, 4]))
    print(mcm([1, 2, 3, 4, 3]))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n + n^2).
    """

    def solve(arr, i, j, dp):
        if i == j:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        min_cost = 1e6
        for k in range(i, j):
            cost = arr[i - 1] * arr[k] * arr[j] + solve(arr, i, k, dp) + solve(arr, k + 1, j, dp)
            min_cost = min(cost, min_cost)
        dp[i][j] = min_cost
        return dp[i][j]

    def mcm(arr):
        n = len(arr)
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        return solve(arr, 1, n - 1, dp)

    print(mcm([10, 20, 30, 40, 50]))
    print(mcm([10, 20, 30, 40]))
    print(mcm([4, 5, 3, 2]))
    print(mcm([10, 15, 20, 25]))
    print(mcm([1, 4, 3, 2]))
    print(mcm([2, 1, 3, 4]))
    print(mcm([1, 2, 3, 4, 3]))


def tabulation():
    """
        Time complexity is O(n^3) and space complexity is O(n^2).
    """

    def mcm(arr):
        n = len(arr)
        dp = {i: {j: 1e6 for j in range(n)} for i in range(n)}
        for i in dp:
            dp[i][i] = 0
        for i in range(n - 1, 0, -1):
            for j in range(1, n):
                if i >= j:
                    continue
                min_cost = 1e6
                for k in range(i, j):
                    cost = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]
                    min_cost = min(cost, min_cost)
                dp[i][j] = min_cost
        return dp[1][n - 1]

    print(mcm([10, 20, 30, 40, 50]))
    print(mcm([10, 20, 30, 40]))
    print(mcm([4, 5, 3, 2]))
    print(mcm([10, 15, 20, 25]))
    print(mcm([1, 4, 3, 2]))
    print(mcm([2, 1, 3, 4]))
    print(mcm([1, 2, 3, 4, 3]))


recursive()
print()
memoized()
print()
tabulation()
