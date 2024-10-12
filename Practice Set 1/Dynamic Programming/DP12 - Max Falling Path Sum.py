def recursive():
    """
        Time complexity is O(3^{mn}) and space complexity is O(m + n)
    """

    def solve(mtx, i, j, n, m):
        if i == 0:
            return mtx[0][j]

        left = -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            left = solve(mtx, i - 1, j - 1, n, m)

        middle = -1e6
        if 0 <= i - 1 < n and 0 <= j < m:
            middle = solve(mtx, i - 1, j, n, m)

        right = -1e6
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            right = solve(mtx, i - 1, j + 1, n, m)

        return mtx[i][j] + max(left, middle, right)

    def max_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_val = -1e6
        for j in range(m):
            max_val = max(max_val, solve(mtx, n - 1, j, n, m))
        return max_val

    print(
        max_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path(
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
        Time complexity is O(mn) and space complexity is O(m + n + mn)
    """

    def solve(mtx, i, j, n, m, dp):
        if i == 0:
            return mtx[0][j]

        if dp[i][j] is not None:
            return dp[i][j]

        left = -1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            left = solve(mtx, i - 1, j - 1, n, m, dp)

        middle = -1e6
        if 0 <= i - 1 < n and 0 <= j < m:
            middle = solve(mtx, i - 1, j, n, m, dp)

        right = -1e6
        if 0 <= i - 1 < n and 0 <= j + 1 < m:
            right = solve(mtx, i - 1, j + 1, n, m, dp)

        dp[i][j] = mtx[i][j] + max(left, middle, right)
        return dp[i][j]

    def max_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_val = -1e6
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        for j in range(m):
            max_val = max(max_val, solve(mtx, n - 1, j, n, m, dp))
        return max_val

    print(
        max_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path(
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
        Time complexity is O(mn) and space complexity is O(mn)
    """
    def max_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_val = -1e6
        dp = {i: {j: -1e6 for j in range(m)} for i in range(n)}
        for j in dp[0]:
            dp[0][j] = mtx[0][j]

        for i in range(1, n):
            for j in range(m):
                left = -1e6
                if 0 <= i - 1 < n and 0 <= j - 1 < m:
                    left = dp[i - 1][j - 1]

                middle = -1e6
                if 0 <= i - 1 < n and 0 <= j < m:
                    middle = dp[i - 1][j]

                right = -1e6
                if 0 <= i - 1 < n and 0 <= j + 1 < m:
                    right = dp[i - 1][j + 1]

                dp[i][j] = mtx[i][j] + max(left, middle, right)

        for j in range(m):
            max_val = max(max_val, dp[n - 1][j])
        return max_val

    print(
        max_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


def space_optimized():
    """
        Time complexity is O(mn) and space complexity is O(m)
    """
    def max_path(mtx):
        n, m = len(mtx), len(mtx[0])
        max_val = -1e6
        prev = {j: -1e6 for j in range(m)}
        for j in prev:
            prev[j] = mtx[0][j]

        for i in range(1, n):
            curr = {j: -1e6 for j in range(m)}
            for j in range(m):
                left = -1e6
                if 0 <= i - 1 < n and 0 <= j - 1 < m:
                    left = prev[j - 1]

                middle = -1e6
                if 0 <= i - 1 < n and 0 <= j < m:
                    middle = prev[j]

                right = -1e6
                if 0 <= i - 1 < n and 0 <= j + 1 < m:
                    right = prev[j + 1]

                curr[j] = mtx[i][j] + max(left, middle, right)
            prev = curr

        for j in range(m):
            max_val = max(max_val, prev[j])
        return max_val

    print(
        max_path(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path(
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
space_optimized()