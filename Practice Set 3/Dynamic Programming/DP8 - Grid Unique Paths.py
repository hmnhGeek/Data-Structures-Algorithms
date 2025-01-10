def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(n + m).
    """
    def solve(i, j, n, m):
        if i == 0:
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

    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """
    def solve(i, j, n, m, dp):
        if i == 0:
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

    print(grid_unique_paths(2, 2))
    print(grid_unique_paths(1, 1))
    print(grid_unique_paths(3, 2))
    print(grid_unique_paths(1, 6))
    print(grid_unique_paths(3, 7))


recursive()
print()
memoized()
print()
