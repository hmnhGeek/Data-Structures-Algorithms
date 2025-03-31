# Question - https://www.youtube.com/watch?v=N_aJ5qQbYA0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=14

def recursive():
    '''
        The overall time complexity would be O(m*(3^n)) = O(3^n) and space complexity would also be O(n).
        Why no m in space complexity? because the paths are vertically travelled, which means in any path there
        will only be n cells for each m. At a time (when m is fixed), the worst case recursion stack can be called
        n times hence, O(n) & not O(mn).
    '''
    def solve_max_path(mtx, i, j, num_cols):
        # since there is a j + 1 in the recursion calls, we need to check for right boundaries also.
        # because we need to find the max path sum, out of bounds should have a negative infinity weight.
        if i < 0 or j not in range(num_cols):
            return float('-inf')

        # if you reach the 0th row from the last row, return the weight of whatever cell you are at.
        if i == 0:
            return mtx[0][j]

        # otherwise, add the current cell weight and branch out to three recursive calls
        # 1. upper-left
        # 2. upper
        # 3. upper-right
        # and get the one which gives the max sum.
        return mtx[i][j] + max(
            solve_max_path(mtx, i - 1, j - 1, num_cols),
            solve_max_path(mtx, i - 1, j, num_cols),
            solve_max_path(mtx, i - 1, j + 1, num_cols)
        )

    def max_path_sum(mtx):
        # according to the question, from (i, j) we can move to
        # (i + 1, j - 1)
        # (i + 1, j)
        # (i + 1, j + 1)
        # but we will reverse the approach and from last row, we will
        # move towards the first row and so, from any (i, j) cell, we can move to the following
        # (i - 1, j - 1)
        # (i - 1, j)
        # (i - 1, j + 1)
        # out of these we will get the max as answer

        # if n = number of rows and m is the number of columns
        n = len(mtx)
        m = len(mtx[0])

        answer = float('-inf')
        for j in range(m):
            answer = max(answer, solve_max_path(mtx, n - 1, j, m))

        return answer

    print(
        max_path_sum(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


def memoized():
    '''
        The overall time complexity would be O(m*n) and space complexity would also be O(n*m + n).
        This time m has a contributing factor because there's no 3^n. Also, in space complexity we
        have m*n due to dp matrix and single n for recursion stack.
    '''
    def solve_max_path(mtx, i, j, num_cols, dp):
        # since there is a j + 1 in the recursion calls, we need to check for right boundaries also.
        # because we need to find the max path sum, out of bounds should have a negative infinity weight.
        if i < 0 or j not in range(num_cols):
            return float('-inf')

        # if you reach the 0th row from the last row, return the weight of whatever cell you are at.
        if i == 0:
            return mtx[0][j]

        if dp[i][j] is not None:
            return dp[i][j]

        # otherwise, add the current cell weight and branch out to three recursive calls
        # 1. upper-left
        # 2. upper
        # 3. upper-right
        # and get the one which gives the max sum.
        dp[i][j] = mtx[i][j] + max(
            solve_max_path(mtx, i - 1, j - 1, num_cols, dp),
            solve_max_path(mtx, i - 1, j, num_cols, dp),
            solve_max_path(mtx, i - 1, j + 1, num_cols, dp)
        )
        return dp[i][j]

    def max_path_sum(mtx):
        # according to the question, from (i, j) we can move to
        # (i + 1, j - 1)
        # (i + 1, j)
        # (i + 1, j + 1)
        # but we will reverse the approach and from last row, we will
        # move towards the first row and so, from any (i, j) cell, we can move to the following
        # (i - 1, j - 1)
        # (i - 1, j)
        # (i - 1, j + 1)
        # out of these we will get the max as answer

        # if n = number of rows and m is the number of columns
        n = len(mtx)
        m = len(mtx[0])
        dp = [[None for _ in range(m)] for _ in range(n)]

        answer = float('-inf')
        for j in range(m):
            answer = max(answer, solve_max_path(mtx, n - 1, j, m, dp))

        return answer

    print(
        max_path_sum(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


def tabulation():
    '''
        The overall time complexity would be O(m*n) and space complexity would also be O(n*m).
        This time m has a contributing factor because there's no 3^n. Also, in space complexity we
        have m*n due to dp matrix.
    '''

    def max_path_sum(mtx):
        # according to the question, from (i, j) we can move to
        # (i + 1, j - 1)
        # (i + 1, j)
        # (i + 1, j + 1)
        # but we will reverse the approach and from last row, we will
        # move towards the first row and so, from any (i, j) cell, we can move to the following
        # (i - 1, j - 1)
        # (i - 1, j)
        # (i - 1, j + 1)
        # out of these we will get the max as answer

        # if n = number of rows and m is the number of columns
        n = len(mtx)
        m = len(mtx[0])
        dp = [[float('-inf') for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[0][j] = mtx[0][j]
                else:
                    # in else block, i > 0, check only for j.

                    upper_left = float('-inf')
                    upper = dp[i - 1][j]
                    upper_right = float('-inf')

                    if j > 0:
                        upper_left = dp[i - 1][j - 1]
                    if j < m - 1:
                        upper_right = dp[i - 1][j + 1]

                    dp[i][j] = mtx[i][j] + max(upper_left, upper, upper_right)

        return max(dp[n - 1])

    print(
        max_path_sum(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


def space_optimized():
    '''
        The overall time complexity would be O(m*n) and space complexity would also be O(m).
        This time m has a contributing factor because there's no 3^n in the time complexity.
        Also, in space complexity we have m elements in the prev array & so, only O(m) space and
        no recursion stack is used.
    '''

    def max_path_sum(mtx):
        # according to the question, from (i, j) we can move to
        # (i + 1, j - 1)
        # (i + 1, j)
        # (i + 1, j + 1)
        # but we will reverse the approach and from last row, we will
        # move towards the first row and so, from any (i, j) cell, we can move to the following
        # (i - 1, j - 1)
        # (i - 1, j)
        # (i - 1, j + 1)
        # out of these we will get the max as answer

        # if n = number of rows and m is the number of columns
        n = len(mtx)
        m = len(mtx[0])
        prev = [float('-inf') for _ in range(m)]

        for i in range(n):
            curr = [float('-inf') for _ in range(m)]
            for j in range(m):
                if i == 0:
                    curr[j] = mtx[0][j]
                else:
                    # in else block, i > 0, check only for j.

                    upper_left = float('-inf')
                    upper = prev[j]
                    upper_right = float('-inf')

                    if j > 0:
                        upper_left = prev[j - 1]
                    if j < m - 1:
                        upper_right = prev[j + 1]

                    curr[j] = mtx[i][j] + max(upper_left, upper, upper_right)
            prev = curr

        # return the max from previous row, that's the answer.
        return max(prev)

    print(
        max_path_sum(
            [
                [1, 2, 10, 4],
                [100, 3, 2, 1],
                [1, 1, 20, 2],
                [1, 2, 2, 1]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 2, 3],
                [3, 7, 2],
                [8, 1, 5]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [1, 2, 3],
                [9, 8, 7],
                [4, 5, 6]
            ]
        )
    )

    print(
        max_path_sum(
            [
                [10, 10, 2, -13, 20, 4],
                [1, -9, -81, 30, 2, 5],
                [0, 10, 4, -79, 2, -10],
                [1, -5, 2, 20, -11, 4]
            ]
        )
    )


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()