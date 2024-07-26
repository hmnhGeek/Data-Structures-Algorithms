# Question - https://www.youtube.com/watch?v=SrP-PiLSYC0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=12

def recursive():
    '''
        Time complexity is O(2^(n^2)) because we have 1 + 2 + 3 + 4 + 5 + --- + n cells and for each cell
        we have two options.
        Space complexity is O(n^2 + n).
    '''
    def solve_triangle_path(triangle, i, j):
        # ensure that i, j don't become negative.
        # an additional test is for the right boundary, ensure that
        # j does not cross the right boundary of the given row.
        # in any of these case return infinite as they are out of bounds.
        if i < 0 or j < 0 or j >= len(triangle[i]):
            return float('inf')
        if i == 0 and j == 0:
            return triangle[0][0]

        # based on the problem, you can only move up or up-left.
        # find the minimum answer from both and add it to triangle[i][j] value.
        return triangle[i][j] + min(
            solve_triangle_path(triangle, i - 1, j),
            solve_triangle_path(triangle, i - 1, j - 1)
        )

    def min_triangle_path_sum(triangle):
        # we will start from the last row in the triangle and go upto 0th index.
        i_max = len(triangle) - 1

        # this function would call the recursion for each cell in the last row.
        # storing j_max (from the last row) to run a loop and get the overall minimum.
        j_max = len(triangle[-1])
        answer = float('inf')

        for j in range(j_max):
            # for each cell in the last row, make recursive calls and find the min
            # distance possible path till 0th index. Hence, i_max is a constant,
            # and j is changing.
            sub = solve_triangle_path(triangle, i_max, j)
            answer = min(answer, sub)

        # finally return the answer
        return answer

    print(
        min_triangle_path_sum(
            [
                [1],
                [2, 3],
                [3, 6, 7],
                [8, 9, 6, 10]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [-10]
            ]
        )
    )


def memoized():
    '''
        Time complexity is O(n(n+1)/2) = O(n^2) because we have 1 + 2 + 3 + 4 + 5 + --- + n cells and for each cell
        we have two options.
        Space complexity is O(n^2 + n).
    '''
    def solve_triangle_path(triangle, i, j, dp):
        # ensure that i, j don't become negative.
        # an additional test is for the right boundary, ensure that
        # j does not cross the right boundary of the given row.
        # in any of these case return infinite as they are out of bounds.
        if i < 0 or j < 0 or j >= len(triangle[i]):
            return float('inf')
        if i == 0 and j == 0:
            return triangle[0][0]

        if dp[i][j] is not None:
            return dp[i][j]

        # based on the problem, you can only move up or up-left.
        # find the minimum answer from both and add it to triangle[i][j] value.
        dp[i][j] = triangle[i][j] + min(
            solve_triangle_path(triangle, i - 1, j, dp),
            solve_triangle_path(triangle, i - 1, j - 1, dp)
        )
        return dp[i][j]

    def min_triangle_path_sum(triangle):
        # we will start from the last row in the triangle and go upto 0th index.
        i_max = len(triangle) - 1

        # this function would call the recursion for each cell in the last row.
        # storing j_max (from the last row) to run a loop and get the overall minimum.
        j_max = len(triangle[-1])
        answer = float('inf')

        # construct the dp array.
        dp = []
        for i in range(len(triangle)):
            dp.append([None for _ in range(len(triangle[i]))])

        for j in range(j_max):
            # for each cell in the last row, make recursive calls and find the min
            # distance possible path till 0th index. Hence, i_max is a constant,
            # and j is changing.
            sub = solve_triangle_path(triangle, i_max, j, dp)
            answer = min(answer, sub)

        # finally return the answer
        return answer

    print(
        min_triangle_path_sum(
            [
                [1],
                [2, 3],
                [3, 6, 7],
                [8, 9, 6, 10]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [-10]
            ]
        )
    )


def tabulation():
    '''
        Time complexity is O(n^2) because we have 1 + 2 + 3 + 4 + 5 + --- + n cells and for each cell
        we have two options.
        Space complexity is O(n^2) but recursion space is avoided.
    '''
    def min_triangle_path_sum(triangle):
        # we will start from the last row in the triangle and go upto 0th index.
        i_max = len(triangle) - 1

        # construct the dp array.
        dp = []
        for i in range(len(triangle)):
            dp.append([None for _ in range(len(triangle[i]))])

        # iterate over all the rows of the triangle
        for i in range(i_max + 1):
            # for each row, iterate over its columns.
            for j in range(len(triangle[i])):
                # BASE CASE
                if i == 0 and j == 0:
                    dp[i][j] = triangle[0][0]
                else:
                    left = float('inf')
                    up_left = float('inf')

                    # i > 0 check is redundant because if i == 0, j will be 0 for sure,
                    # because in the first row, there's only one element. Thus, this case
                    # would be handled in if condition. However, explicitly writing it
                    # here for code readability.
                    if i > 0:
                        # ensure that for the previous row, j is not outflowing from the right
                        if j in range(len(triangle[i - 1])):
                            left = dp[i - 1][j]

                        # ensure that for the previous row j is not outflowing from left.
                        # basically if you are on the leftest column, j - 1 from the previous
                        # row cannot exist. Please check using an example.
                        if j in range(1, len(triangle[i - 1])):
                            up_left = dp[i - 1][j - 1]

                    dp[i][j] = triangle[i][j] + min(left, up_left)

        # finally return the min value in the last row of the dp matrix.
        return min(dp[i_max])

    print(
        min_triangle_path_sum(
            [
                [1],
                [2, 3],
                [3, 6, 7],
                [8, 9, 6, 10]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [-10]
            ]
        )
    )


def tabulation2():
    '''
        Time complexity is O(n^2) because we have 1 + 2 + 3 + 4 + 5 + --- + n cells and for each cell
        we have two options.
        Space complexity is O(n^2) but recursion space is avoided.
    '''
    def min_triangle_path_sum(triangle):
        # we will start from the last row in the triangle and go upto 0th index.
        i_max = len(triangle) - 1

        # construct the dp array but this time with some additional space.
        # basically construct a matrix of size n*n and not just a triangular
        # dp array. This is beneficial because we won't need to check for
        # boundaries of j.
        dp = [[float('inf') for _ in range(i_max + 1)] for _ in range(i_max + 1)]

        # iterate over all the rows of the triangle
        for i in range(i_max + 1):
            # for each row, iterate over its columns.
            for j in range(len(triangle[i])):
                # BASE CASE
                if i == 0 and j == 0:
                    dp[i][j] = triangle[0][0]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        # finally return the min value in the last row of the dp matrix.
        return min(dp[i_max])

    print(
        min_triangle_path_sum(
            [
                [1],
                [2, 3],
                [3, 6, 7],
                [8, 9, 6, 10]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [-10]
            ]
        )
    )


def space_optimized():
    '''
        Time complexity is O(n^2) because we have 1 + 2 + 3 + 4 + 5 + --- + n cells and for each cell
        we have two options.
        Space complexity is O(n) where n denotes the number of elements in the last row of the triangle.
        Both ns in the time and space complexity here are the same.
    '''
    def min_triangle_path_sum(triangle):
        # we will start from the last row in the triangle and go upto 0th index.
        i_max = len(triangle) - 1
        prev = [float('inf') for _ in range(len(triangle[i_max]))]

        # iterate over all the rows of the triangle
        for i in range(i_max + 1):
            # for each row, iterate over its columns.
            curr = [float('inf') for _ in range(len(triangle[i_max]))]
            for j in range(len(triangle[i])):
                # BASE CASE
                if i == 0 and j == 0:
                    curr[j] = triangle[0][0]
                else:
                    # we need not worry about bounds of j, because we initialized
                    # prev row of length equal to the length of the last row.
                    # Also, for out of bounds, by default prev row contains infinite.
                    curr[j] = triangle[i][j] + min(prev[j], prev[j - 1])
            prev = curr

        # finally return the min value in the last row of the dp matrix.
        return min(prev)

    print(
        min_triangle_path_sum(
            [
                [1],
                [2, 3],
                [3, 6, 7],
                [8, 9, 6, 10]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
            ]
        )
    )

    print(
        min_triangle_path_sum(
            [
                [-10]
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
print("Better tabulation (tabulation2) solution with a n x n dp matrix")
tabulation2()

print()
print("Space optimized solution using tabulation2()")
space_optimized()

