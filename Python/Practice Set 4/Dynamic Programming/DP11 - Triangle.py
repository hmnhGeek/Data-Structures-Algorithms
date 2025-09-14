def recursive():
    """
        Time complexity is O(2^{nm}) and space complexity is O(n + m).
    """
    def triangle(mtx):
        n = len(mtx)
        result = 1e6
        for last_elem_idx in range(n):
            ans = solve(mtx, n - 1, last_elem_idx)
            result = min(result, ans)
        return result

    def solve(mtx, i, j):
        if i == 0 and j == 0:
            return mtx[0][0]
        up = 1e6
        if i - 1 >= 0 and j <= i - 1:
            up = mtx[i][j] + solve(mtx, i - 1, j)
        diagonal = 1e6
        if j - 1 >= 0 and i - 1 >= 0:
            diagonal = mtx[i][j] + solve(mtx, i - 1, j - 1)
        return min(up, diagonal)

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
print()
