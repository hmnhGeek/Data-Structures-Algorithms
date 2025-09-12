def recursive():
    def min_path_sum(mtx):
        """
            Time complexity is O(2^{mn}) and space complexity is O(m + n).
        """
        n, m = len(mtx), len(mtx[0])
        return solve(mtx, n - 1, m - 1)

    def solve(mtx, i, j):
        if i == 0 and j == 0:
            return mtx[0][0]
        left = 1e6
        if 0 <= j - 1:
            left = mtx[i][j] + solve(mtx, i, j - 1)
        right = 1e6
        if 0 <= i - 1:
            right = mtx[i][j] + solve(mtx, i - 1, j)
        return min(left, right)

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
    def min_path_sum(mtx):
        """
            Time complexity is O(mn) and space complexity is O(m + n + mn).
        """
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve(mtx, n - 1, m - 1, dp)

    def solve(mtx, i, j, dp):
        if i == 0 and j == 0:
            return mtx[0][0]
        if dp[i][j] is not None:
            return dp[i][j]
        left = 1e6
        if 0 <= j - 1:
            left = mtx[i][j] + solve(mtx, i, j - 1, dp)
        right = 1e6
        if 0 <= i - 1:
            right = mtx[i][j] + solve(mtx, i - 1, j, dp)
        dp[i][j] = min(left, right)
        return dp[i][j]

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
    def min_path_sum(mtx):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """
        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: 1e6 for j in range(m)} for i in range(n)}
        dp[0][0] = mtx[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + mtx[i][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] + mtx[0][j]

        for i in range(1, n):
            for j in range(1, m):
                left = 1e6
                if 0 <= j - 1:
                    left = mtx[i][j] + dp[i][j - 1]
                right = 1e6
                if 0 <= i - 1:
                    right = mtx[i][j] + dp[i - 1][j]
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
    def min_path_sum(mtx):
        """
            Time complexity is O(mn) and space complexity is O(m).
        """
        n, m = len(mtx), len(mtx[0])
        prev = {j: 1e6 for j in range(m)}
        prev[0] = mtx[0][0]
        for j in range(1, m):
            prev[j] = prev[j - 1] + mtx[0][j]

        for i in range(1, n):
            curr = {j: 1e6 for j in range(m)}
            curr[0] = prev[0] + mtx[i][0]
            for j in range(1, m):
                left = 1e6
                if 0 <= j - 1:
                    left = mtx[i][j] + curr[j - 1]
                right = 1e6
                if 0 <= i - 1:
                    right = mtx[i][j] + prev[j]
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
print()
