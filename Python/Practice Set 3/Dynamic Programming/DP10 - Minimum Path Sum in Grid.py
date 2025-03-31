# Problem link - https://leetcode.com/problems/minimum-path-sum/description/
# Solution - https://www.youtube.com/watch?v=_rgTlyky1uQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=11


def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(n + m).
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


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """

    def solve(mtx, i, j, n, m, dp):
        if i == 0 and j == 0:
            return mtx[0][0]
        if dp[i][j] is not None:
            return dp[i][j]
        left = 1e6
        if 0 <= i - 1 < n:
            left = mtx[i][j] + solve(mtx, i - 1, j, n, m, dp)
        right = 1e6
        if 0 <= j - 1 < m:
            right = mtx[i][j] + solve(mtx, i, j - 1, n, m, dp)
        dp[i][j] = min(left, right)
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


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def min_path_sum(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: 1e6 for j in range(m)} for i in range(n)}
        dp[0][0] = mtx[0][0]
        for i in range(n):
            for j in range(m):
                if i == j == 0:
                    continue
                left = 1e6
                if 0 <= i - 1 < n:
                    left = mtx[i][j] + dp[i - 1][j]
                right = 1e6
                if 0 <= j - 1 < m:
                    right = mtx[i][j] + dp[i][j - 1]
                dp[i][j] = min(left, right)
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


def space_optimized():
    """
        Time complexity is O(nm) and space complexity is O(m).
    """
    def min_path_sum(mtx):
        n, m = len(mtx), len(mtx[0])
        prev = {j: 1e6 for j in range(m)}
        prev[0] = mtx[0][0]
        for i in range(n):
            curr = {j: 1e6 for j in range(m)}
            curr[0] = mtx[i][0]
            for j in range(m):
                if i == j == 0:
                    continue
                left = 1e6
                if 0 <= i - 1 < n:
                    left = mtx[i][j] + prev[j]
                right = 1e6
                if 0 <= j - 1 < m:
                    right = mtx[i][j] + curr[j - 1]
                curr[j] = min(left, right)
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
print()
memoized()
print()
tabulation()
print()
space_optimized()
