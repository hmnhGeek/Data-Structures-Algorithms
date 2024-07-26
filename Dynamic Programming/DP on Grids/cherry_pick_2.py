# Question - https://www.youtube.com/watch?v=QGfn7JeXK54&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=14

def recursive():
    '''
        At each (i, j) there are 9 cases and there will be "n" vertical paths (n = number of rows).
        There will be m^2 starting points. Hence, the time complexity is O(m^2 * 9^n).
        Space complexity would be O(n) for the recursion stack space.

         Each recursion level stores m^2 states, but this is transient and does not multiply with the recursion depth.
    '''

    def f(i, j1, j2, mtx, num_cols):
        # if you get beyond 0th row, return -inf
        if i < 0:
            return -1e6

        # if either or both alice and bob are out of bounds, return -inf
        if j1 not in range(num_cols) or j2 not in range(num_cols):
            return -1e6

        # if they both reached 0th row, but are not at their starting points,
        # i.e., alice is not on (0, 0) and bob is not on (0, num_cols - 1),
        # return -inf.
        if i == 0 and (j1 != 0 or j2 != num_cols - 1):
            return -1e6

        # if alice is at (0, 0) and bob is at (0, num_cols - 1), return
        # the sum of chocolates at their starting points.
        if i == 0 and j1 == 0 and j2 == num_cols - 1:
            return mtx[0][0] + mtx[0][num_cols - 1]

        # for this particular call, assume that the number of chocolates accumulated
        # is -infinity.
        maxi = -1e6

        # since alice and bob are moving upwards, they both will have common i.
        # however, if alice moves to j1 - 1, there will be 3 possible cases for bob
        # namely, j2 - 1, j2, j2 + 1. Same 3 cases will be there when alice moves
        # j1 and j1 + 1. In total, there would be 9 cases. We could write if-else
        # to write those 9 cases, or we know that delta in j directions is -1, 0, 1.
        # we introduce dj1 & dj2 to denote deltas in alice and bob horizontal movements.
        # By doing this nested for loop, we can cover those 9 cases.
        for dj1 in [-1, 0, 1]:
            for dj2 in [-1, 0, 1]:
                # if for the current call, both alice and bob are on the same cell, just
                # add number of chocolates once from that cell and move to the upper row
                # by adding deltas in their respective j values.
                if j1 == j2:
                    maxi = max(maxi, mtx[i][j1] + f(i - 1, j1 + dj1, j2 + dj2, mtx, num_cols))
                else:
                    # if they are not on the same cell, add chocolates from both their cells,
                    # and move to the upper row by adding deltas in their respective j values.
                    maxi = max(maxi, mtx[i][j1] + mtx[i][j2] + f(i - 1, j1 + dj1, j2 + dj2, mtx, num_cols))

                # in all the 9 cases, continuously update the maximum chocolates that can be obtained

        # return the maximum chocolates that can be obtained.
        return maxi

    def cherry_pick(mtx):
        n, m = len(mtx), len(mtx[0])
        answer = -1e6

        # in the last row, take the all possible "ending" scenarios for alice and bob
        # for each scenario, you will get some output from function "f". There will be m^2
        # calls to function "f", and for each starting point from the "ending row", we will
        # get the maximum number of chocolates. Finally, return the maximum out of these
        # m^2 combinations.
        for j_alice in range(m):
            for j_bob in range(m):
                answer = max(answer, f(n - 1, j_alice, j_bob, mtx, m))

        return answer

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )


def memoized():
    '''
        The time complexity is O(m^2 * n). Notice that now, m^2 has become significant.
        Space complexity would be O([m^2 * n] + n) because we have a 3D dp matrix of dimensions m x m x n,
        and we have a recursion stack space of n.
    '''

    def f(i, j1, j2, mtx, num_cols, dp):
        # if you get beyond 0th row, return -inf
        if i < 0:
            return -1e6

        # if either or both alice and bob are out of bounds, return -inf
        if j1 not in range(num_cols) or j2 not in range(num_cols):
            return -1e6

        # if they both reached 0th row, but are not at their starting points,
        # i.e., alice is not on (0, 0) and bob is not on (0, num_cols - 1),
        # return -inf.
        if i == 0 and (j1 != 0 or j2 != num_cols - 1):
            return -1e6

        # if alice is at (0, 0) and bob is at (0, num_cols - 1), return
        # the sum of chocolates at their starting points.
        if i == 0 and j1 == 0 and j2 == num_cols - 1:
            return mtx[0][0] + mtx[0][num_cols - 1]

        if dp[i][j1][j2] is not None:
            return dp[i][j1][j2]

        # for this particular call, assume that the number of chocolates accumulated
        # is -infinity.
        maxi = -1e6

        # since alice and bob are moving upwards, they both will have common i.
        # however, if alice moves to j1 - 1, there will be 3 possible cases for bob
        # namely, j2 - 1, j2, j2 + 1. Same 3 cases will be there when alice moves
        # j1 and j1 + 1. In total, there would be 9 cases. We could write if-else
        # to write those 9 cases, or we know that delta in j directions is -1, 0, 1.
        # we introduce dj1 & dj2 to denote deltas in alice and bob horizontal movements.
        # By doing this nested for loop, we can cover those 9 cases.
        for dj1 in [-1, 0, 1]:
            for dj2 in [-1, 0, 1]:
                # if for the current call, both alice and bob are on the same cell, just
                # add number of chocolates once from that cell and move to the upper row
                # by adding deltas in their respective j values.
                if j1 == j2:
                    maxi = max(maxi, mtx[i][j1] + f(i - 1, j1 + dj1, j2 + dj2, mtx, num_cols, dp))
                else:
                    # if they are not on the same cell, add chocolates from both their cells,
                    # and move to the upper row by adding deltas in their respective j values.
                    maxi = max(maxi, mtx[i][j1] + mtx[i][j2] + f(i - 1, j1 + dj1, j2 + dj2, mtx, num_cols, dp))

                # in all the 9 cases, continuously update the maximum chocolates that can be obtained

        # return the maximum chocolates that can be obtained.
        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]

    def cherry_pick(mtx):
        n, m = len(mtx), len(mtx[0])
        answer = -1e6
        dp = [[[None for _ in range(m)] for _ in range(m)] for _ in range(n)]

        # in the last row, take the all possible "ending" scenarios for alice and bob
        # for each scenario, you will get some output from function "f". There will be m^2
        # calls to function "f", and for each starting point from the "ending row", we will
        # get the maximum number of chocolates. Finally, return the maximum out of these
        # m^2 combinations.
        for j_alice in range(m):
            for j_bob in range(m):
                answer = max(answer, f(n - 1, j_alice, j_bob, mtx, m, dp))

        return answer

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )


def tabulation():
    '''
        The time complexity is O(m^2 * n). Notice that now, m^2 has become significant.
        Space complexity would be O([m^2 * n]) because we have a 3D dp matrix of dimensions m x m x n,
        and we have removed the recursion stack space of n.
    '''

    def cherry_pick(mtx):
        n, m = len(mtx), len(mtx[0])
        dp = [[[-1e6 for _ in range(m)] for _ in range(m)] for _ in range(n)]

        # Alice is at (0, 0) and Bob is at (0, m - 1). Hence, in this base case, add up total chocolates from the
        # starting positions, i.e., mtx[0][0] + mtx[0][m - 1]
        dp[0][0][m - 1] = mtx[0][0] + mtx[0][m - 1]

        # start from the next row, i.e. 1st index row. This will take O(m^2 * n) time.
        for i in range(1, n):
            for j1 in range(m):
                for j2 in range(m):
                    # in all the 9 cases, continuously update the maximum chocolates that can be obtained
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            # if for the current call, both alice and bob are on the same cell, just
                            # add number of chocolates once from that cell and move to the upper row
                            # by adding deltas in their respective j values.

                            # before that, please check if either of them are out of bounds or not.
                            # if both of them are within matrix, continue.
                            if j1 + dj1 in range(m) and j2 + dj2 in range(m):
                                if j1 == j2:
                                    dp[i][j1][j2] = max(dp[i][j1][j2], mtx[i][j1] + dp[i - 1][j1 + dj1][j2 + dj2])
                                else:
                                    # if they are not on the same cell, add chocolates from both their cells,
                                    # and move to the upper row by adding deltas in their respective j values.
                                    dp[i][j1][j2] = max(dp[i][j1][j2],
                                                        mtx[i][j1] + mtx[i][j2] + dp[i - 1][j1 + dj1][j2 + dj2])

        # the answer will lie in the last matrix stored in the 3D DP matrix. There is no option, but to traverse
        # that last matrix of size m x m. This will thus take O(m^2) time to find the correct answer.
        answer = -1e6
        for j1 in range(m):
            for j2 in range(m):
                answer = max(answer, dp[n - 1][j1][j2])

        return answer

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )


def space_optimized():
    '''
        The time complexity is O(m^2 * n). Notice that now, m^2 has become significant.
        Space complexity would be O(m^2) because we have a `prev` 2D matrix of dimensions m x m,
        and we have removed the n matrices that we stored in the tabulation solution.
    '''

    def cherry_pick(mtx):
        n, m = len(mtx), len(mtx[0])
        prev = [[-1e6 for _ in range(m)] for _ in range(m)]

        # Alice is at (0, 0) and Bob is at (0, m - 1). Hence, in this base case, add up total chocolates from the
        # starting positions, i.e., mtx[0][0] + mtx[0][m - 1]
        prev[0][m - 1] = mtx[0][0] + mtx[0][m - 1]

        # start from the next row, i.e. 1st index row. This will take O(m^2 * n) time.
        for i in range(1, n):
            curr = [[-1e6 for _ in range(m)] for _ in range(m)]
            for j1 in range(m):
                for j2 in range(m):
                    # in all the 9 cases, continuously update the maximum chocolates that can be obtained
                    for dj1 in [-1, 0, 1]:
                        for dj2 in [-1, 0, 1]:
                            # if for the current call, both alice and bob are on the same cell, just
                            # add number of chocolates once from that cell and move to the upper row
                            # by adding deltas in their respective j values.

                            # before that, please check if either of them are out of bounds or not.
                            # if both of them are within matrix, continue.
                            if j1 + dj1 in range(m) and j2 + dj2 in range(m):
                                if j1 == j2:
                                    curr[j1][j2] = max(curr[j1][j2], mtx[i][j1] + prev[j1 + dj1][j2 + dj2])
                                else:
                                    # if they are not on the same cell, add chocolates from both their cells,
                                    # and move to the upper row by adding deltas in their respective j values.
                                    curr[j1][j2] = max(curr[j1][j2], mtx[i][j1] + mtx[i][j2] + prev[j1 + dj1][j2 + dj2])

            prev = curr

        # the answer will lie in the last matrix stored in the 3D DP matrix. There is no option, but to traverse
        # that last matrix of size m x m. This will thus take O(m^2) time to find the correct answer.
        answer = -1e6
        for j1 in range(m):
            for j2 in range(m):
                answer = max(answer, prev[j1][j2])

        return answer

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pick(
            [
                [4, 5],
                [3, 7],
                [4, 2]
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