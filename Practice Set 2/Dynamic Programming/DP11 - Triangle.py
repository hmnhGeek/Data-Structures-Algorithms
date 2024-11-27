def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n).
    """

    def solve(mtx, i, j, n):
        if i == 0 and j == 0:
            return mtx[i][j]

        up = 1e6
        if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
            up = mtx[i][j] + solve(mtx, i - 1, j, n)
        diagonal = 1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
            diagonal = mtx[i][j] + solve(mtx, i - 1, j - 1, n)
        return min(diagonal, up)

    def triangle(mtx):
        n = len(mtx)
        min_path_sum = 1e6
        for j in range(len(mtx[-1]) - 1, -1, -1):
            min_path_sum = min(min_path_sum, solve(mtx, n - 1, j, n))
        return min_path_sum

    print(
        triangle(
            [
                [1],
                [2, 3],
                [3, 6, 7],
                [8, 9, 6, 10]
            ]
        )
    )

    print(
        triangle(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

    print(triangle([[-10]]))

    print(
        triangle(
            [
                [1],
                [2, 3],
                [4, 5, 6],
                [7, 8, 9, 10]
            ]
        )
    )

    print(
        triangle(
            [
                [5],
                [-1, 3],
                [22, 1, -9]
            ]
        )
    )

    print(
        triangle(
            [
                [2],
                [3, 7],
                [8, 5, 6],
                [6, 1, 9, 3]
            ]
        )
    )

    print(
        triangle(
            [
                [3],
                [6, 9],
                [8, 7, 1],
                [9, 6, 8, 2]
            ]
        )
    )


recursive()