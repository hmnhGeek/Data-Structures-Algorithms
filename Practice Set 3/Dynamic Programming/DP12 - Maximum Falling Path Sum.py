def recursive():
    """
        Time complexity is O(3^{nm}) and space complexity is O(n + m).
    """
    def solve(mtx, i, j, n, m):
        if i == 0:
            return mtx[0][j]
        left = -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            left = mtx[i][j] + solve(mtx, i - 1, j - 1, n, m)
        middle = -1e6
        if 0 <= i - 1 < n:
            middle = mtx[i][j] + solve(mtx, i - 1, j, n, m)
        right = -1e6
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            right = mtx[i][j] + solve(mtx, i - 1, j + 1, n, m)
        return max(left, middle, right)

    def max_falling_path(mtx):
        n, m = len(mtx), len(mtx[0])
        ans = -1e6
        for j in range(m):
            cost = solve(mtx, n - 1, j, n, m)
            ans = max(ans, cost)
        return ans

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
        Time complexity is O(nm^2) and space complexity is O(n + m + nm).
    """
    def solve(mtx, i, j, n, m, dp):
        if i == 0:
            return mtx[0][j]
        if dp[i][j] is not None:
            return dp[i][j]
        left = -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            left = mtx[i][j] + solve(mtx, i - 1, j - 1, n, m, dp)
        middle = -1e6
        if 0 <= i - 1 < n:
            middle = mtx[i][j] + solve(mtx, i - 1, j, n, m, dp)
        right = -1e6
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            right = mtx[i][j] + solve(mtx, i - 1, j + 1, n, m, dp)
        dp[i][j] = max(left, middle, right)
        return dp[i][j]

    def max_falling_path(mtx):
        n, m = len(mtx), len(mtx[0])
        ans = -1e6
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        for j in range(m):
            cost = solve(mtx, n - 1, j, n, m, dp)
            ans = max(ans, cost)
        return ans

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