# Problem link - https://www.naukri.com/code360/problems/maze-obstacles_977241?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=TmhpgXScLyY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=10


def recursive():
    def unique_paths(mtx):
        """
            Time complexity is O(2^{m + n}) and space complexity is O(m + n).
        """

        n, m = len(mtx), len(mtx[0])
        return solve(mtx, n - 1, m - 1)

    def solve(mtx, i, j):
        if i < 0 or j < 0:
            return 0
        if mtx[i][j] == -1:
            return 0
        if i == 0 and j == 0:
            return 1
        up = solve(mtx, i - 1, j)
        left = solve(mtx, i, j - 1)
        return up + left

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


def memoized():
    def unique_paths(mtx):
        """
            Time complexity is O(mn) and space complexity is O(m + n + mn).
        """

        n, m = len(mtx), len(mtx[0])
        dp = {i: {j: None for j in range(-1, m)} for i in range(-1, n)}
        return solve(mtx, n - 1, m - 1, dp)

    def solve(mtx, i, j, dp):
        if i < 0 or j < 0:
            return 0
        if mtx[i][j] == -1:
            return 0
        if i == 0 and j == 0:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        up = solve(mtx, i - 1, j, dp)
        left = solve(mtx, i, j - 1, dp)
        dp[i][j] = up + left
        return dp[i][j]

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


def tabulation():
    def unique_paths(mtx):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """

        n, m = len(mtx), len(mtx[0])
        if mtx[0][0] == -1 or mtx[n - 1][m - 1] == -1:
            return 0
        dp = {i: {j: 0 for j in range(-1, m)} for i in range(-1, n)}
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if mtx[i][j] == -1:
                    continue
                up = dp[i - 1][j]
                left = dp[i][j - 1]
                dp[i][j] = up + left
        return dp[n - 1][m - 1]

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
            ]
        )
    )


def space_optimized():
    def unique_paths(mtx):
        """
            Time complexity is O(mn) and space complexity is O(m).
        """
        n, m = len(mtx), len(mtx[0])
        if mtx[0][0] == -1 or mtx[n - 1][m - 1] == -1:
            return 0
        prev = {j: 0 for j in range(-1, m)}
        for i in range(n):
            curr = {j: 0 for j in range(-1, m)}
            if i == 0:
                curr[0] = 1
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if mtx[i][j] == -1:
                    continue
                up = prev[j]
                left = curr[j - 1]
                curr[j] = up + left
            prev = curr
        return prev[m - 1]

    print(
        unique_paths(
            [
                [0, 0, 0],
                [0, -1, 0],
                [0, 0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [-1, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, -1],
                [0, 0]
            ]
        )
    )

    print(
        unique_paths(
            [
                [0, 0, -1, 0, -1],
                [0, 0, 0, -1, 0],
                [-1, 0, 0, -1, 0],
                [0, 0, 0, 0, 0]
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
