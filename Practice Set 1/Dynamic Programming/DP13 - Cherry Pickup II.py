def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n).
    """
    def solve(mtx, row, i, j, n, m):
        if row == 0:
            if i == 0 and j != m - 1:
                return mtx[0][0]
            elif i != 0 and j == m - 1:
                return mtx[0][m - 1]
            elif i == 0 and j == m - 1:
                return mtx[0][0] + mtx[0][m - 1]
            else:
                return 0

        result = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if 0 <= row - 1 < n and 0 <= i + di < m and 0 <= j + dj < m:
                    result = max(result, solve(mtx, row - 1, i + di, j + dj, n, m))
        if i == j:
            return mtx[row][i] + result
        else:
            return mtx[row][i] + mtx[row][j] + result

    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        ans = 0
        for i in range(m):
            for j in range(m):
                ans = max(ans, solve(mtx, n - 1, i, j, n, m))
        return ans

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
        )
    )

    print(cherry_pickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                         [1, 0, 2, 3, 0, 0, 6]]))


def memoized():
    """
        Time complexity is O(nm^2) and space complexity is O(m + n + nm^2).
    """
    def solve(mtx, row, i, j, n, m, dp):
        if row == 0:
            if i == 0 and j != m - 1:
                return mtx[0][0]
            elif i != 0 and j == m - 1:
                return mtx[0][m - 1]
            elif i == 0 and j == m - 1:
                return mtx[0][0] + mtx[0][m - 1]
            else:
                return 0

        if dp[row][i][j] is not None:
            return dp[row][i][j]

        result = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if 0 <= row - 1 < n and 0 <= i + di < m and 0 <= j + dj < m:
                    result = max(result, solve(mtx, row - 1, i + di, j + dj, n, m, dp))
        if i == j:
            dp[row][i][j] = mtx[row][i] + result
        else:
            dp[row][i][j] = mtx[row][i] + mtx[row][j] + result
        return dp[row][i][j]

    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        ans = 0
        dp = {i: {j: {k: None for k in range(m)} for j in range(m)} for i in range(n)}
        for i in range(m):
            for j in range(m):
                ans = max(ans, solve(mtx, n - 1, i, j, n, m, dp))
        return ans

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
        )
    )

    print(cherry_pickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                         [1, 0, 2, 3, 0, 0, 6]]))


def tabulation():
    """
        Time complexity is O(nm^2) and space complexity is O(nm^2).
    """
    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        ans = 0
        dp = {i: {j: {k: 0 for k in range(m)} for j in range(m)} for i in range(n)}

        # define dp for 1st row; base case
        for j in dp[0][0]:
            if j != m - 1:
                dp[0][0][j] = mtx[0][0]
            else:
                dp[0][0][j] = mtx[0][0] + mtx[0][m - 1]
        for i in dp[0]:
            if i != 0:
                for j in dp[0][i]:
                    if j == m - 1:
                        dp[0][i][j] = mtx[0][m - 1]

        # start from 1st row.
        for row in range(1, n):
            for i in range(m):
                for j in range(m):
                    result = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if 0 <= row - 1 < n and 0 <= i + di < m and 0 <= j + dj < m:
                                result = max(result, dp[row - 1][i + di][j + dj])
                    if i == j:
                        dp[row][i][j] = mtx[row][i] + result
                    else:
                        dp[row][i][j] = mtx[row][i] + mtx[row][j] + result

        # loop on the last row of the dp
        for i in range(m):
            for j in range(m):
                ans = max(ans, dp[n - 1][i][j])
        return ans

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
        )
    )

    print(cherry_pickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                         [1, 0, 2, 3, 0, 0, 6]]))


recursive()
print()
memoized()
print()
tabulation()
