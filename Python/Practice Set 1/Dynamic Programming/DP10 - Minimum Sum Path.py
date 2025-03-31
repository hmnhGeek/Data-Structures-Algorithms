# Problem link - https://www.naukri.com/code360/problems/minimum-path-sum_985349?source=youtube&campaign=striver_dp_videos


def recursive():
    """
        Time complexity is O(2^{mn}) and space complexity is O(m + n)
    """

    def solve(mtx, i, j, n, m):
        if i == 0 and j == 0:
            return mtx[0][0]

        left = 1e6
        if 0 <= i - 1 < n:
            left = solve(mtx, i - 1, j, n, m)

        right = 1e6
        if 0 <= j - 1 < m:
            right = solve(mtx, i, j - 1, n, m)

        return mtx[i][j] + min(left, right)

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
                [1, 2],
            ]
        )
    )


def memoized():
    """
        Time complexity is O(m*n) and space complexity is O(m + n + m*n)
    """

    def solve(mtx, i, j, n, m, dp):
        if i == 0 and j == 0:
            return mtx[0][0]

        if dp[i][j] is not None:
            return dp[i][j]

        left = 1e6
        if 0 <= i - 1 < n:
            left = solve(mtx, i - 1, j, n, m, dp)

        right = 1e6
        if 0 <= j - 1 < m:
            right = solve(mtx, i, j - 1, n, m, dp)

        dp[i][j] = mtx[i][j] + min(left, right)
        return dp[i][j]

    def min_path_sum(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve(mtx, n - 1, m - 1, n, m, dp)

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
                [1, 2],
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(m*n) and space complexity is O(m*n)
    """

    def min_path_sum(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: 1e6 for j in range(m)} for i in range(n)}

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = mtx[0][0]
                else:
                    left = 1e6
                    if 0 <= i - 1 < n:
                        left = dp[i - 1][j]

                    right = 1e6
                    if 0 <= j - 1 < m:
                        right = dp[i][j - 1]

                    dp[i][j] = mtx[i][j] + min(left, right)

        return dp[n - 1][m - 1]

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
                [1, 2],
            ]
        )
    )


def space_optimized():
    """
        Time complexity is O(m*n) and space complexity is O(m)
    """

    def min_path_sum(mtx):
        n, m = len(mtx), len(mtx[0])
        prev = {j: 1e6 for j in range(m)}

        for i in range(n):
            curr = {j: 1e6 for j in range(m)}
            for j in range(m):
                if i == 0 and j == 0:
                    curr[0] = mtx[0][0]
                else:
                    left = 1e6
                    if 0 <= i - 1 < n:
                        left = prev[j]

                    right = 1e6
                    if 0 <= j - 1 < m:
                        right = curr[j - 1]
                    curr[j] = mtx[i][j] + min(left, right)
            prev = curr
        return prev[m - 1]

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
                [1, 2],
            ]
        )
    )

    print(
        min_path_sum(
            [
                [1, 2, 3],
                [4, 8, 2],
                [1, 5, 3]
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