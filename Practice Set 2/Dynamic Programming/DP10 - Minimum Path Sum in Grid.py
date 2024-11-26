def recursive():
    """
        Time complexity is O(2^{mn}) and space complexity is O(m + n).
    """
    def solve(mtx, i, j, n, m):
        if i == 0 and j == 0:
            return mtx[0][0]

        left = 1e6
        if 0 <= i - 1 < n:
            left = mtx[i][j] + solve(mtx, i - 1, j, n, m)
        right = 1e6
        if 0 <= j - 1 < m:
            right = mtx[i][j] + solve(mtx, i, j - 1, n, m)
        return min(left, right)

    def min_path_sum(mtx):
        n, m = len(mtx), len(mtx[0])
        return solve(mtx, n - 1, m - 1, n, m)

    print(
        min_path_sum(
            [
                [5, 9, 6],
                [11, 5, 2]
            ]
        )
    )

    print(
        min_path_sum(
            [
                [5]
            ]
        )
    )

    print(
        min_path_sum(
            [
                [1, 2, 3],
                [4, 5, 4],
                [7, 5, 9]
            ]
        )
    )

    print(
        min_path_sum(
            [
                [5, 6],
                [1, 2]
            ]
        )
    )

    print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(min_path_sum([[1, 2, 3], [4, 5, 6]]))


recursive()
