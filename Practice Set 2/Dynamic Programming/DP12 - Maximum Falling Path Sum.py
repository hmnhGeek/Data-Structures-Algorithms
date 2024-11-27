def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n).
    """

    def solve(mtx, i, j, n, m):
        if i == 0:
            return mtx[0][j]

        up_left = -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            up_left = mtx[i][j] + solve(mtx, i - 1, j - 1, n, m)

        up = -1e6
        if 0 <= i - 1 < n:
            up = mtx[i][j] + solve(mtx, i - 1, j, n, m)

        up_right = -1e6
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            up_right = mtx[i][j] + solve(mtx, i - 1, j + 1, n, m)

        return max(up_left, up, up_right)

    def max_falling_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_sum_path = -1e6
        for k in range(m):
            max_sum_path = max(max_sum_path, solve(mtx, n - 1, k, n, m))
        return max_sum_path

    print(
        max_falling_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(m^2 * n) and space complexity is O(m + n + mn).
    """

    def solve(mtx, i, j, n, m, dp):
        if i == 0:
            return mtx[0][j]

        if dp[i][j] is not None:
            return dp[i][j]

        up_left = -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            up_left = mtx[i][j] + solve(mtx, i - 1, j - 1, n, m, dp)

        up = -1e6
        if 0 <= i - 1 < n:
            up = mtx[i][j] + solve(mtx, i - 1, j, n, m, dp)

        up_right = -1e6
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            up_right = mtx[i][j] + solve(mtx, i - 1, j + 1, n, m, dp)

        dp[i][j] = max(up_left, up, up_right)
        return dp[i][j]

    def max_falling_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_sum_path = -1e6
        for k in range(m):
            dp = {i: {j: None for j in range(m)} for i in range(n)}
            max_sum_path = max(max_sum_path, solve(mtx, n - 1, k, n, m, dp))
        return max_sum_path

    print(
        max_falling_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(m^2 * n) and space complexity is O(mn).
    """
    def max_falling_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_sum_path = -1e6
        for k in range(m):
            dp = {i: {j: -1e6 for j in range(m)} for i in range(n)}
            for j in range(m):
                dp[0][j] = mtx[0][j]
            for i in range(1, n):
                for j in range(m):
                    up_left = -1e6
                    if 0 <= i - 1 < n and 0 <= j - 1 < m:
                        up_left = mtx[i][j] + dp[i - 1][j - 1]

                    up = -1e6
                    if 0 <= i - 1 < n:
                        up = mtx[i][j] + dp[i - 1][j]

                    up_right = -1e6
                    if 0 <= i - 1 < n and 0 <= j + 1 < m:
                        up_right = mtx[i][j] + dp[i - 1][j + 1]

                    dp[i][j] = max(up_left, up, up_right)
            max_sum_path = max(max_sum_path, dp[n - 1][k])
        return max_sum_path

    print(
        max_falling_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_falling_path(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


recursive()
print()
memoized()
print()
tabulation()
