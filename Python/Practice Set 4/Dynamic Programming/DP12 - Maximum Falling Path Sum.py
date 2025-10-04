def recursive():
    def max_falling_path(mtx):
        """
            Time complexity is exponential and space complexity is O(m + n).
        """
        n, m = len(mtx), len(mtx[0])
        result = -1e6
        for k in range(m):
            sub_result = solve(mtx, n - 1, k, n, m)
            result = max(result, sub_result)
        return result

    def solve(mtx, i, j, n, m):
        if i == 0:
            return mtx[i][j]
        left, up, right = -1e6, -1e6, -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            left = solve(mtx, i - 1, j - 1, n, m)
        if 0 <= i - 1 < n:
            up = solve(mtx, i - 1, j, n, m)
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            right = solve(mtx, i - 1, j + 1, n, m)
        return mtx[i][j] + max(left, up, right)

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
    def max_falling_path(mtx):
        """
            Time complexity is O(m^2 * n) and space complexity is O(m + n + mn).
        """
        n, m = len(mtx), len(mtx[0])
        result = -1e6
        for k in range(m):
            dp = {i: {j: None for j in range(m)} for i in range(n)}
            sub_result = solve(mtx, n - 1, k, n, m, dp)
            result = max(result, sub_result)
        return result

    def solve(mtx, i, j, n, m, dp):
        if i == 0:
            return mtx[i][j]
        if dp[i][j] is not None:
            return dp[i][j]
        left, up, right = -1e6, -1e6, -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            left = solve(mtx, i - 1, j - 1, n, m, dp)
        if 0 <= i - 1 < n:
            up = solve(mtx, i - 1, j, n, m, dp)
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            right = solve(mtx, i - 1, j + 1, n, m, dp)
        dp[i][j] = mtx[i][j] + max(left, up, right)
        return dp[i][j]

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
    def max_falling_path(mtx):
        """
            Time complexity is O(m^2 * n) and space complexity is O(mn).
        """
        n, m = len(mtx), len(mtx[0])
        result = -1e6
        for k in range(m):
            dp = {i: {j: -1e6 for j in range(m)} for i in range(n)}
            for j in range(m):
                dp[0][j] = mtx[0][j]

            for i in range(1, n):
                for j in range(m):
                    left, up, right = -1e6, -1e6, -1e6
                    if 0 <= i - 1 < n and 0 <= j - 1 < m:
                        left = dp[i - 1][j - 1]
                    if 0 <= i - 1 < n:
                        up = dp[i - 1][j]
                    if 0 <= i - 1 < n and 0 <= j + 1 < m:
                        right = dp[i - 1][j + 1]
                    dp[i][j] = mtx[i][j] + max(left, up, right)

            sub_result = dp[n - 1][k]
            result = max(result, sub_result)
        return result

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
print()
