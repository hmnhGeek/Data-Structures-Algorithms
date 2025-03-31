# Problem link - https://www.geeksforgeeks.org/minimum-sum-path-triangle/
# Solution - https://www.youtube.com/watch?v=SrP-PiLSYC0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=12


def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n).
    """

    def solve(mtx, i, j, n):
        if i == 0 and j == 0:
            return mtx[i][j]

        up = 1e6
        if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
            up = mtx[i][j] + solve(mtx, i - 1, j, n)
        diagonal = 1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
            diagonal = mtx[i][j] + solve(mtx, i - 1, j - 1, n)
        return min(diagonal, up)

    def triangle(mtx):
        n = len(mtx)
        min_path_sum = 1e6
        for j in range(len(mtx[-1]) - 1, -1, -1):
            min_path_sum = min(min_path_sum, solve(mtx, n - 1, j, n))
        return min_path_sum

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


def memoized():
    """
        Time complexity is O(m^2 *n) and space complexity is O(m + n + mn).
    """

    def solve(mtx, i, j, n, dp):
        if i == 0 and j == 0:
            return mtx[i][j]

        if dp[i][j] is not None:
            return dp[i][j]

        up = 1e6
        if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
            up = mtx[i][j] + solve(mtx, i - 1, j, n, dp)
        diagonal = 1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
            diagonal = mtx[i][j] + solve(mtx, i - 1, j - 1, n, dp)
        dp[i][j] = min(diagonal, up)
        return dp[i][j]

    def triangle(mtx):
        n = len(mtx)
        min_path_sum = 1e6
        dp = {i: {j: None for j in range(len(mtx[i]))} for i in range(n)}

        # O(m) time X O(mn) = O(m^2 *n)
        for j in range(len(mtx[-1]) - 1, -1, -1):
            min_path_sum = min(min_path_sum, solve(mtx, n - 1, j, n, dp))
        return min_path_sum

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


def tabulation():
    """
        Time complexity is O(m^2 * n) and space complexity is O(mn).
    """
    def triangle(mtx):
        n = len(mtx)
        min_path_sum = 1e6
        dp = {i: {j: 1e6 for j in range(len(mtx[i]))} for i in range(n)}
        dp[0][0] = mtx[0][0]

        # O(m) X O(n) X O(m) = O(m^2 * n)
        for k in range(len(mtx[-1]) - 1, -1, -1):
            for i in range(1, n):
                for j in range(len(mtx[i])):
                    up = 1e6
                    if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
                        up = mtx[i][j] + dp[i - 1][j]
                    diagonal = 1e6
                    if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
                        diagonal = mtx[i][j] + dp[i - 1][j - 1]
                    dp[i][j] = min(diagonal, up)
            min_path_sum = min(min_path_sum, dp[n - 1][k])
        return min_path_sum

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


def space_optimized():
    """
        Time complexity is O(m^2 * n) and space complexity is O(m).
    """
    def triangle(mtx):
        n = len(mtx)
        min_path_sum = 1e6
        for k in range(len(mtx[-1]) - 1, -1, -1):
            prev = {0: mtx[0][0]}
            for i in range(1, n):
                curr = {j: 1e6 for j in range(len(mtx[i]))}
                for j in range(len(mtx[i])):
                    up = 1e6
                    if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
                        up = mtx[i][j] + prev[j]
                    diagonal = 1e6
                    if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
                        diagonal = mtx[i][j] + prev[j - 1]
                    curr[j] = min(diagonal, up)
                prev = curr
            min_path_sum = min(min_path_sum, prev[k])
        return min_path_sum

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
memoized()
print()
tabulation()
print()
space_optimized()
