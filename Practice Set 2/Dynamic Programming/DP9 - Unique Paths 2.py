def recursive():
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


recursive()
