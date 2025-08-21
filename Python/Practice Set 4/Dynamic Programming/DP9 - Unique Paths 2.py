def recursive():
    def unique_paths(mtx):
        """
            Time complexity is O(2^{m + n}) and space complexity is O(m + n).
        """

        n, m = len(mtx), len(mtx[0])
        return solve(mtx, n - 1, m - 1)

    def solve(mtx, i, j):
        if i < 0 or j < 0:
            return 0
        if mtx[i][j] == -1:
            return 0
        if i == 0 and j == 0:
            return 1
        up = solve(mtx, i - 1, j)
        left = solve(mtx, i, j - 1)
        return up + left

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
    def unique_paths(mtx):
        """
            Time complexity is O(mn) and space complexity is O(m + n + mn).
        """

        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: None for j in range(-1, m)} for i in range(-1, n)}
        return solve(mtx, n - 1, m - 1, dp)

    def solve(mtx, i, j, dp):
        if i < 0 or j < 0:
            return 0
        if mtx[i][j] == -1:
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        up = solve(mtx, i - 1, j, dp)
        left = solve(mtx, i, j - 1, dp)
        dp[i][j] = up + left
        return dp[i][j]

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