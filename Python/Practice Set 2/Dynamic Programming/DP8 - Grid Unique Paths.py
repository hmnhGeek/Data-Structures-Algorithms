# Problem link - https://www.naukri.com/code360/problems/total-unique-paths_1081470
# Solution - https://www.youtube.com/watch?v=sdE0A2Oxofw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=9


def recursive():
    # Time complexity is O(2^{nm}) and space complexity is O(m + n)
    def solve(i, j, n, m):
        if i == 0 and j == 0:
            return 1

        left = 0
        if 0 <= i - 1 < n:
            left = solve(i - 1, j, n, m)
        right = 0
        if 0 <= j - 1 < m:
            right = solve(i, j - 1, n, m)
        return left + right

    def grid_unique_paths(n, m):
        return solve(n - 1, m - 1, n, m)

    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


def memoized():
    # Time complexity is O(nm) and space complexity is O(m + n + mn)
    def solve(i, j, n, m, dp):
        if i == 0 and j == 0:
            return 1

        if dp[i][j] is not None:
            return dp[i][j]

        left = 0
        if 0 <= i - 1 < n:
            left = solve(i - 1, j, n, m, dp)
        right = 0
        if 0 <= j - 1 < m:
            right = solve(i, j - 1, n, m, dp)
        dp[i][j] = left + right
        return dp[i][j]

    def grid_unique_paths(n, m):
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve(n - 1, m - 1, n, m, dp)

    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


def tabulation():
    # Time complexity is O(nm) and space complexity is O(mn)
    def grid_unique_paths(n, m):
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue
                left = 0
                if 0 <= i - 1 < n:
                    left = dp[i - 1][j]
                right = 0
                if 0 <= j - 1 < m:
                    right = dp[i][j - 1]
                dp[i][j] = left + right
        return dp[n - 1][m - 1]

    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


def space_optimized():
    # Time complexity is O(nm) and space complexity is O(m)
    def grid_unique_paths(n, m):
        prev = {j: 1 for j in range(m)}
        for i in range(n):
            curr = {j: 0 for j in range(m)}
            curr[0] = 1
            for j in range(m):
                if i == j == 0:
                    continue
                left = 0
                if 0 <= i - 1 < n:
                    left = prev[j]
                right = 0
                if 0 <= j - 1 < m:
                    right = curr[j - 1]
                curr[j] = left + right
            prev = curr
        return prev[m - 1]

    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
