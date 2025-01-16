def recursive():
    """
        Time complexity is O(2^{nm}) and space complexity is O(n + m).
    """
    def solve(mtx, i, j, n):
        if i == j == 0:
            return mtx[0][0]
        left = 1e6
        if 0 <= i - 1 < n and 0 <= j < i:
            left = mtx[i][j] + solve(mtx, i - 1, j, n)
        right = 1e6
        if 0 <= i - 1 < n and j >= 1:
            right = mtx[i][j] + solve(mtx, i - 1, j - 1, n)
        return min(left, right)

    def triangle(mtx):
        n = len(mtx)
        min_ans = 1e6
        for j in range(n):
            cost = solve(mtx, n - 1, j, n)
            min_ans = min(min_ans, cost)
        return min_ans

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
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """
    def solve(mtx, i, j, n, dp):
        if i == j == 0:
            return mtx[0][0]
        if dp[i][j] is not None:
            return dp[i][j]
        left = 1e6
        if 0 <= i - 1 < n and 0 <= j < i:
            left = mtx[i][j] + solve(mtx, i - 1, j, n, dp)
        right = 1e6
        if 0 <= i - 1 < n and j >= 1:
            right = mtx[i][j] + solve(mtx, i - 1, j - 1, n, dp)
        dp[i][j] = min(left, right)
        return dp[i][j]

    def triangle(mtx):
        n = len(mtx)
        min_ans = 1e6
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        for j in range(n):
            cost = solve(mtx, n - 1, j, n, dp)
            min_ans = min(min_ans, cost)
        return min_ans

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
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def triangle(mtx):
        n = len(mtx)
        min_ans = 1e6
        dp = {i: {j: 1e6 for j in range(n)} for i in range(n)}
        dp[0][0] = mtx[0][0]
        for max_j in range(n):
            for i in range(n):
                for j in range(max_j + 1):
                    if i == j == 0:
                        continue
                    left = 1e6
                    if 0 <= i - 1 < n and 0 <= j < i:
                        left = mtx[i][j] + dp[i - 1][j]
                    right = 1e6
                    if 0 <= i - 1 < n and 0 <= j - 1 < i:
                        right = mtx[i][j] + dp[i - 1][j - 1]
                    dp[i][j] = min(left, right)
            cost = dp[n - 1][max_j]
            min_ans = min(min_ans, cost)
        return min_ans

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