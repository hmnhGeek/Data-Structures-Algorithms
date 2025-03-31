# Problem link - https://www.naukri.com/code360/problems/triangle_1229398?source=youtube&campaign=striver_dp_videos


def recursive():
    """
        T: O(2^{nm}) and space is O(n + m)
    """
    def solve(mtx, i, j, n):
        if i == 0 and j == 0:
            return mtx[0][0]

        left = 1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
            left = solve(mtx, i - 1, j - 1, n)

        right = 1e6
        if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
            right = solve(mtx, i - 1, j, n)

        return mtx[i][j] + min(left, right)

    def triangle(mtx):
        n = len(mtx)
        m = len(mtx[-1])
        min_cost = 1e6
        for j in range(m):
            min_cost = min(min_cost, solve(mtx, n - 1, j, n))
        return min_cost

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

    print(
        triangle(
            [[-10]]
        )
    )

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


def memoized():
    """
        T: O(mn) and space is O(n + m + mn)
    """
    def solve(mtx, i, j, n, dp):
        if i == 0 and j == 0:
            return mtx[0][0]

        if dp[i][j] is not None:
            return dp[i][j]

        left = 1e6
        if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
            left = solve(mtx, i - 1, j - 1, n, dp)

        right = 1e6
        if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
            right = solve(mtx, i - 1, j, n, dp)

        dp[i][j] = mtx[i][j] + min(left, right)
        return dp[i][j]

    def triangle(mtx):
        n = len(mtx)
        m = len(mtx[-1])
        min_cost = 1e6
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        for j in range(m):
            min_cost = min(min_cost, solve(mtx, n - 1, j, n, dp))
        return min_cost

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

    print(
        triangle(
            [[-10]]
        )
    )

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


def tabulation():
    """
        T: O(mn) and space is O(mn)
    """
    def triangle(mtx):
        n = len(mtx)
        m = len(mtx[-1])
        min_cost = 1e6
        dp = {i: {j: 1e6 for j in range(len(mtx[i]))} for i in range(n)}
        dp[0][0] = mtx[0][0]

        for i in range(1, n):
            for j in range(len(mtx[i])):
                left = 1e6
                if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
                    left = dp[i - 1][j - 1]

                right = 1e6
                if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
                    right = dp[i - 1][j]
                dp[i][j] = mtx[i][j] + min(left, right)

        for j in range(m):
            min_cost = min(min_cost, dp[n - 1][j])
        return min_cost

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

    print(
        triangle(
            [[-10]]
        )
    )

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


def space_optimized():
    """
        T: O(mn) and space is O(m)
    """
    def triangle(mtx):
        n = len(mtx)
        m = len(mtx[-1])
        min_cost = 1e6
        prev = {j: 1e6 for j in range(1)}
        prev[0] = mtx[0][0]

        for i in range(1, n):
            curr = {j: 1e6 for j in range(len(mtx[i]))}
            for j in range(len(mtx[i])):
                left = 1e6
                if 0 <= i - 1 < n and 0 <= j - 1 < len(mtx[i - 1]):
                    left = prev[j - 1]

                right = 1e6
                if 0 <= i - 1 < n and 0 <= j < len(mtx[i - 1]):
                    right = prev[j]
                curr[j] = mtx[i][j] + min(left, right)
            prev = curr

        for j in range(m):
            min_cost = min(min_cost, prev[j])
        return min_cost

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

    print(
        triangle(
            [[-10]]
        )
    )

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


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()