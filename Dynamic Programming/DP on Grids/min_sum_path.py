# Question - https://www.youtube.com/watch?v=_rgTlyky1uQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=11

def recursive():
    '''
        Time complexity of this solution would be O(2^(mn))
        Space complexity of this solution would be O(2^(mn))
    '''
    def get_min_path_solve(mtx, i, j):
        # if you were able to reach (0, 0), return the cell weight at (0, 0)
        if i == 0 and j == 0:
            return mtx[0][0]

        # if you get out of bounds of matrix, return infinity so that you
        # disregard it in `min()` calls further in the recursion
        if i < 0 or j < 0:
            return float('inf')

        # finally, return path weight which would be the sum of current cell's weight
        # plus minimum weight obtained by doing recursions on left and upper cells.
        return mtx[i][j] + min(
            get_min_path_solve(mtx, i - 1, j),
            get_min_path_solve(mtx, i, j - 1)
        )

    def get_min_path(mtx):
        n, m = len(mtx), len(mtx[0])
        return get_min_path_solve(mtx, n - 1, m - 1)


    print(
        get_min_path(
            [
                [5, 9, 6],
                [11, 5, 2]
            ]
        )
    )

    print(
        get_min_path([[5]])
    )

    print(
        get_min_path(
            [
                [1, 2, 3],
                [4, 5, 4],
                [7, 5, 9]
            ]
        )
    )

    print(
        get_min_path(
            [
                [5, 6],
                [1, 2]
            ]
        )
    )


def memoized():
    '''
        Time complexity of this solution would be O(m*n)
        Space complexity of this solution would be O(m*n) + O(m + n) where m + n denotes total number of paths.
    '''
    def get_min_path_solve(mtx, i, j, dp):
        # if you were able to reach (0, 0), return the cell weight at (0, 0)
        if i == 0 and j == 0:
            return mtx[0][0]

        # if you get out of bounds of matrix, return infinity so that you
        # disregard it in `min()` calls further in the recursion
        if i < 0 or j < 0:
            return float('inf')

        if dp[i][j] is not None:
            return dp[i][j]

        # finally, return path weight which would be the sum of current cell's weight
        # plus minimum weight obtained by doing recursions on left and upper cells.
        dp[i][j] = mtx[i][j] + min(
            get_min_path_solve(mtx, i - 1, j, dp),
            get_min_path_solve(mtx, i, j - 1, dp)
        )
        return dp[i][j]

    def get_min_path(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = [[None for _ in range(m)] for _ in range(n)]
        return get_min_path_solve(mtx, n - 1, m - 1, dp)


    print(
        get_min_path(
            [
                [5, 9, 6],
                [11, 5, 2]
            ]
        )
    )

    print(
        get_min_path([[5]])
    )

    print(
        get_min_path(
            [
                [1, 2, 3],
                [4, 5, 4],
                [7, 5, 9]
            ]
        )
    )

    print(
        get_min_path(
            [
                [5, 6],
                [1, 2]
            ]
        )
    )


def tabulation():
    '''
        Time complexity of this solution would be O(m*n)
        Space complexity of this solution would be O(m*n)
    '''
    def get_min_path(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = [[None for _ in range(m)] for _ in range(n)]
        dp[0][0] = mtx[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = mtx[0][0]
                else:
                    left = float('inf')
                    up = float('inf')

                    if i > 0:
                        up = dp[i - 1][j]
                    if j > 0:
                        left = dp[i][j - 1]

                    dp[i][j] = mtx[i][j] + min(left, up)

        return dp[-1][-1]

    print(
        get_min_path(
            [
                [5, 9, 6],
                [11, 5, 2]
            ]
        )
    )

    print(
        get_min_path([[5]])
    )

    print(
        get_min_path(
            [
                [1, 2, 3],
                [4, 5, 4],
                [7, 5, 9]
            ]
        )
    )

    print(
        get_min_path(
            [
                [5, 6],
                [1, 2]
            ]
        )
    )


def space_optimized():
    '''
        Time complexity of this solution would be O(m*n)
        Space complexity of this solution would be O(m) because we are just storing the previous row.
    '''
    def get_min_path(mtx):
        n, m = len(mtx), len(mtx[0])

        # store the previous row which is out of bounds with infinities
        prev = [float('inf') for _ in range(m)]

        for i in range(n):
            curr = [float('inf') for _ in range(m)]
            for j in range(m):
                if i == 0 and j == 0:
                    curr[0] = mtx[0][0]
                else:
                    left = float('inf')
                    up = float('inf')

                    if i > 0:
                        up = prev[j]
                    if j > 0:
                        left = curr[j - 1]

                    curr[j] = mtx[i][j] + min(left, up)
            prev = curr

        return prev[-1]

    print(
        get_min_path(
            [
                [5, 9, 6],
                [11, 5, 2]
            ]
        )
    )

    print(
        get_min_path([[5]])
    )

    print(
        get_min_path(
            [
                [1, 2, 3],
                [4, 5, 4],
                [7, 5, 9]
            ]
        )
    )

    print(
        get_min_path(
            [
                [5, 6],
                [1, 2]
            ]
        )
    )


print()
print("Recursive solution")
recursive()

print()
print("Memoization solution")
memoized()

print()
print("Tabulation solution")
tabulation()

print()
print("Space optimized solution")
space_optimized()