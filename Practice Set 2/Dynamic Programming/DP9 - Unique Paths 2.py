def recursive():
    """
        Time complexity is O(2^{mn}) and space complexity is O(m + n).
    """
    def solve(mtx, i, j, n, m):
        if i == 0 and j == 0:
            return 1 if mtx[0][0] == 0 else 0
        if mtx[i][j] != 0:
            return 0
        left = 0
        if 0 <= i - 1 < n:
            left = solve(mtx, i - 1, j, n, m)
        right = 0
        if 0 <= j - 1 < m:
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


def memoized():
    """
        Time complexity is O(mn) and space complexity is O(m + n + mn).
    """
    def solve(mtx, i, j, n, m, dp):
        if i == 0 and j == 0:
            return 1 if mtx[0][0] == 0 else 0

        if dp[i][j] is not None:
            return dp[i][j]

        if mtx[i][j] != 0:
            return 0
        left = 0
        if 0 <= i - 1 < n:
            left = solve(mtx, i - 1, j, n, m, dp)
        right = 0
        if 0 <= j - 1 < m:
            right = solve(mtx, i, j - 1, n, m, dp)
        dp[i][j] = left + right
        return dp[i][j]

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


def tabulation():
    """
        Time complexity is O(mn) and space complexity is O(mn).
    """
    def unique_paths(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}

        obstacle_found = False
        for i in range(n):
            if mtx[i][0] != 0:
                obstacle_found = True
                break
        if obstacle_found:
            for i in range(1, n):
                dp[i][0] = 0
        else:
            for i in range(1, n):
                dp[i][0] = 1

        obstacle_found = False
        for j in range(m):
            if mtx[0][j] != 0:
                obstacle_found = True
                break
        if obstacle_found:
            for j in range(1, m):
                dp[0][j] = 0
        else:
            for j in range(1, m):
                dp[0][j] = 1

        dp[0][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if mtx[i][j] != 0:
                    dp[i][j] = 0
                else:
                    left = 0
                    if 0 <= i - 1 < n:
                        left = dp[i - 1][j]
                    right = 0
                    if 0 <= j - 1 < m:
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


recursive()
print()
memoized()
print()
tabulation()
