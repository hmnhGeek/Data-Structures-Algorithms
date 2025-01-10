def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(n + m).
    """
    def solve(mtx, i, j, n, m):
        if i == 0 and j == 0:
            return 1
        left = 0
        if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
            left = solve(mtx, i - 1, j, n, m)
        right = 0
        if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
            right = solve(mtx, i, j - 1, n, m)
        return left + right

    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        if mtx[0][0] == -1 or mtx[n - 1][m - 1] == -1:
            return 0
        return solve(mtx, n - 1, m - 1, n, m)

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """
    def solve(mtx, i, j, n, m, dp):
        if i == 0 and j == 0:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        left = 0
        if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
            left = solve(mtx, i - 1, j, n, m, dp)
        right = 0
        if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
            right = solve(mtx, i, j - 1, n, m, dp)
        dp[i][j] = left + right
        return dp[i][j]

    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        if mtx[0][0] == -1 or mtx[n - 1][m - 1] == -1:
            return 0
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve(mtx, n - 1, m - 1, n, m, dp)

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        if mtx[0][0] == -1 or mtx[n - 1][m - 1] == -1:
            return 0
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                    continue
                left = 0
                if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
                    left = dp[i - 1][j]
                right = 0
                if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
                    right = dp[i][j - 1]
                dp[i][j] = left + right
        return dp[n - 1][m - 1]

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


def space_optimized():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        if mtx[0][0] == -1 or mtx[n - 1][m - 1] == -1:
            return 0
        prev = {j: 0 for j in range(m)}
        prev[0] = 1
        for i in range(n):
            curr = {j: 0 for j in range(m)}
            curr[0] = prev[0]
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                left = 0
                if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
                    left = prev[j]
                right = 0
                if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
                    right = curr[j - 1]
                curr[j] = left + right
            prev = curr
        return prev[m - 1]

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
