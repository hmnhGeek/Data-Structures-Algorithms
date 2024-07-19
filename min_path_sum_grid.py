def recursive():
    def solve_min_path_sum(mtx, x, y):
        # if you are at (0, 0), return the value of that cell
        if x == 0 and y == 0:
            return mtx[0][0]

        # since we want to find the minimum cost, maximize left and up with infinity each.
        left, up = float('inf'), float('inf')

        # if left cell is in mtx
        if y - 1 >= 0:
            left = solve_min_path_sum(mtx, x, y - 1)

        # if upper cell is in mtx
        if x - 1 >= 0:
            up = solve_min_path_sum(mtx, x - 1, y)

        # add the current cell value with the min path cost from left or up.
        return mtx[x][y] + min(left, up)

    def min_path_sum(mtx):
        R, C = len(mtx), len(mtx[0])
        return solve_min_path_sum(mtx, R - 1, C - 1)

    print(min_path_sum([[5, 9, 6], [11, 5, 2]]))
    print(min_path_sum([[5]]))
    print(min_path_sum([[1, 2, 3], [4, 5, 4], [7, 5, 9]]))
    print(min_path_sum([[5, 6], [1, 2]]))


def memoized():
    def solve_min_path_sum(mtx, x, y, dp):
        # if you are at (0, 0), return the value of that cell
        if x == 0 and y == 0:
            return mtx[0][0]

        if dp[x][y] is not None:
            return dp[x][y]

        # since we want to find the minimum cost, maximize left and up with infinity each.
        left, up = float('inf'), float('inf')

        # if left cell is in mtx
        if y - 1 >= 0:
            left = solve_min_path_sum(mtx, x, y - 1, dp)

        # if upper cell is in mtx
        if x - 1 >= 0:
            up = solve_min_path_sum(mtx, x - 1, y, dp)

        # add the current cell value with the min path cost from left or up.
        dp[x][y] = mtx[x][y] + min(left, up)
        return dp[x][y]

    def min_path_sum(mtx):
        R, C = len(mtx), len(mtx[0])
        dp = [[None for _ in range(C)] for _ in range(R)]
        return solve_min_path_sum(mtx, R - 1, C - 1, dp)

    print(min_path_sum([[5, 9, 6], [11, 5, 2]]))
    print(min_path_sum([[5]]))
    print(min_path_sum([[1, 2, 3], [4, 5, 4], [7, 5, 9]]))
    print(min_path_sum([[5, 6], [1, 2]]))


def tabulation():
    def min_path_sum(mtx):
        R, C = len(mtx), len(mtx[0])
        dp = [[None for _ in range(C)] for _ in range(R)]

        dp[0][0] = mtx[0][0]

        for x in range(R):
            for y in range(C):
                if x == 0 and y == 0:
                    # if you are at (0, 0), make dp[0][0] = mtx[0][0]
                    dp[0][0] = mtx[0][0]
                else:
                    # since we want to find the minimum cost, maximize left and up with infinity each.
                    left, up = float('inf'), float('inf')

                    # if left cell is in mtx
                    if y - 1 >= 0:
                        left = dp[x][y - 1]

                    # if upper cell is in mtx
                    if x - 1 >= 0:
                        up = dp[x - 1][y]

                    # add the current cell value with the min path cost from left or up.
                    dp[x][y] = mtx[x][y] + min(left, up)

        return dp[R - 1][C - 1]

    print(min_path_sum([[5, 9, 6], [11, 5, 2]]))
    print(min_path_sum([[5]]))
    print(min_path_sum([[1, 2, 3], [4, 5, 4], [7, 5, 9]]))
    print(min_path_sum([[5, 6], [1, 2]]))


def space_optimized():
    def min_path_sum(mtx):
        R, C = len(mtx), len(mtx[0])

        # create a blank last row
        prev = [0 for _ in range(C)]

        for x in range(R):
            # create a blank current row
            curr = [0 for _ in range(C)]
            for y in range(C):
                if x == 0 and y == 0:
                    # if you are at (0, 0), make dp[0][0] = mtx[0][0]
                    curr[0] = mtx[0][0]
                else:
                    # since we want to find the minimum cost, maximize left and up with infinity each.
                    left, up = float('inf'), float('inf')

                    # if left cell is in mtx
                    if y - 1 >= 0:
                        left = curr[y - 1]

                    # if upper cell is in mtx
                    if x - 1 >= 0:
                        up = prev[y]

                    # add the current cell value with the min path cost from left or up.
                    curr[y] = mtx[x][y] + min(left, up)

            # in the next iteration, curr becomes prev
            prev = curr

        # answer lies in the last index of the previous row.
        return prev[C - 1]

    print(min_path_sum([[5, 9, 6], [11, 5, 2]]))
    print(min_path_sum([[5]]))
    print(min_path_sum([[1, 2, 3], [4, 5, 4], [7, 5, 9]]))
    print(min_path_sum([[5, 6], [1, 2]]))


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