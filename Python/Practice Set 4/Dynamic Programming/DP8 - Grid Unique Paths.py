def recursive():
    """
        Time complexity is O(2 ^ {m + n}) and space complexity is O(n + m).
    """

    def get_paths(n, m):
        return solve(n - 1, m - 1)

    def solve(i, j):
        if i < 0 or j < 0:
            return 0
        if i == 0 and j == 0:
            return 1
        up = solve(i - 1, j)
        down = solve(i, j - 1)
        return up + down

    print(get_paths(3, 7))
    print(get_paths(3, 2))
    print(get_paths(2, 2))
    print(get_paths(2, 3))


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """

    def get_paths(n, m):
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve(n - 1, m - 1, dp)

    def solve(i, j, dp):
        if i < 0 or j < 0:
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        up = solve(i - 1, j, dp)
        down = solve(i, j - 1, dp)
        dp[i][j] = up + down
        return dp[i][j]

    print(get_paths(3, 7))
    print(get_paths(3, 2))
    print(get_paths(2, 2))
    print(get_paths(2, 3))


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """

    def get_paths(n, m):
        dp = {i: {j: 0 for j in range(-1, m)} for i in range(-1, n)}
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                up = dp[i - 1][j]
                down = dp[i][j - 1]
                dp[i][j] = up + down
        return dp[n - 1][m - 1]

    print(get_paths(3, 7))
    print(get_paths(3, 2))
    print(get_paths(2, 2))
    print(get_paths(2, 3))


recursive()
print()
memoized()
print()
tabulation()
