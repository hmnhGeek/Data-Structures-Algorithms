# Problem link - https://www.naukri.com/code360/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=mO8XpGoJwuo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=25


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(arr, i, j):
        if j == 0:
            return 0
        if i == 0:
            return j * arr[0]
        left = -1e6
        if i + 1 <= j:
            left = arr[i] + solve(arr, i, j - i - 1)
        right = solve(arr, i - 1, j)
        return max(left, right)

    def rod_cut(costs, rod_length):
        n = len(costs)
        return solve(costs, n - 1, rod_length)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n + 2n).
    """
    def solve(arr, i, j, dp):
        if j == 0:
            return 0
        if i == 0:
            return j * arr[0]
        if dp[i][j] is not None:
            return dp[i][j]
        left = -1e6
        if i + 1 <= j:
            left = arr[i] + solve(arr, i, j - i - 1, dp)
        right = solve(arr, i - 1, j, dp)
        dp[i][j] = max(left, right)
        return dp[i][j]

    def rod_cut(costs, rod_length):
        n = len(costs)
        dp = {i: {j: None for j in range(rod_length + 1)} for i in range(n)}
        return solve(costs, n - 1, rod_length, dp)

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n^2).
    """
    def rod_cut(costs, rod_length):
        n = len(costs)
        dp = {i: {j: -1e6 for j in range(rod_length + 1)} for i in range(n)}
        for i in dp:
            dp[i][0] = 0
        for j in dp[0]:
            dp[0][j] = j * costs[0]
        for i in range(1, n):
            for j in range(rod_length + 1):
                left = -1e6
                if i + 1 <= j:
                    left = costs[i] + dp[i][j - i - 1]
                right = dp[i - 1][j]
                dp[i][j] = max(left, right)
        return dp[n - 1][rod_length]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


def space_optimized():
    """
        Time complexity is O(n^2) and space complexity is O(n).
    """
    def rod_cut(costs, rod_length):
        n = len(costs)
        prev = {j: -1e6 for j in range(rod_length + 1)}
        prev[0] = 0
        for j in prev:
            prev[j] = j * costs[0]
        for i in range(1, n):
            curr = {j: -1e6 for j in range(rod_length + 1)}
            curr[0] = 0
            for j in range(rod_length + 1):
                left = -1e6
                if i + 1 <= j:
                    left = costs[i] + curr[j - i - 1]
                right = prev[j]
                curr[j] = max(left, right)
            prev = curr
        return prev[rod_length]

    print(rod_cut([2, 5, 7, 8, 10], 5))
    print(rod_cut([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3, 5, 6, 7, 10, 12], 6))
    print(rod_cut([1, 10, 3, 1, 3, 1, 5, 9], 8))
    print(rod_cut([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(rod_cut([3], 1))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
