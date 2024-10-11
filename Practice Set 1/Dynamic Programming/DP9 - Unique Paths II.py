def recursive():
    def solve(mtx, i, j, n, m):
        # Time complexity is exponential and space complexity is O(n + m)

        if i == 0 and j == 0:
            return 1

        left = 0
        if 0 <= i - 1 < n and mtx[i - 1][j] != -1:
            left = solve(mtx, i - 1, j, n, m)

        right = 0
        if 0 <= j - 1 < m and mtx[i][j - 1] != -1:
            right = solve(mtx, i, j - 1, n, m)

        return left + right

    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
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


def memoized():
    def solve(mtx, i, j, n, m, dp):
        # Time complexity is O(n*m) and space complexity is O(n + m + n*m)

        if i == 0 and j == 0:
            return 1

        if dp[i][j] is not None:
            return dp[i][j]

        left = 0
        if 0 <= i - 1 < n and mtx[i - 1][j] != -1:
            left = solve(mtx, i - 1, j, n, m, dp)

        right = 0
        if 0 <= j - 1 < m and mtx[i][j - 1] != -1:
            right = solve(mtx, i, j - 1, n, m, dp)

        dp[i][j] = left + right
        return left + right

    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
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


def tabulation():
    """
        Time complexity is O(nm) and space complexity O(nm).
    """
    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    left = 0
                    if 0 <= i - 1 < n and mtx[i - 1][j] != -1:
                        left = dp[i - 1][j]

                    right = 0
                    if 0 <= j - 1 < m and mtx[i][j - 1] != -1:
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


def space_optimized():
    """
        Time complexity is O(nm) and space complexity O(m).
    """
    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        prev = {j: 0 for j in range(m)}
        for j in prev:
            if mtx[0][j] == 0:
                prev[j] = 1

        for i in range(1, n):
            curr = {j: 0 for j in range(m)}
            curr[0] = 1 if mtx[i][0] == 0 else 0
            for j in range(1, m):
                left = 0
                if 0 <= i - 1 < n and mtx[i - 1][j] != -1:
                    left = prev[j]

                right = 0
                if 0 <= j - 1 < m and mtx[i][j - 1] != -1:
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


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()