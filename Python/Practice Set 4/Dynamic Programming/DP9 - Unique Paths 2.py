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


recursive()
print()