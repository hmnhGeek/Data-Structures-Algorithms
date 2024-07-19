def recursive():
    # In recursion, we usually follow top-down approach.
    # Therefore, start from index (R - 1, C - 1) till (0, 0)
    # Basically, if question mentioned that the directions are right and down
    # in recursion we will move left and up to reach (0, 0).
    def solve_unique_paths(x, y):
        # at any point, if you reach (0, 0), return 1 to denote one found path
        if x == 0 and y == 0:
            return 1

        # if at any point, you're out of bounds of the matrix, return 0 possible paths
        elif x < 0 or y < 0:
            return 0

        # check all possible paths from left and up and add them and return.
        return solve_unique_paths(x, y - 1) + solve_unique_paths(x - 1, y)

    def get_num_unique_paths(R, C):
        return solve_unique_paths(R - 1, C - 1)

    print(get_num_unique_paths(2, 2))
    print(get_num_unique_paths(2, 3))
    print(get_num_unique_paths(3, 3))


def memoized():
    def solve_unique_paths(x, y, dp):
        # classical memoization approach in solving the previous recursive question
        if x == 0 and y == 0:
            return 1
        elif x < 0 or y < 0:
            return 0

        if dp[x][y] is not None:
            return dp[x][y]

        dp[x][y] = solve_unique_paths(x, y - 1, dp) + solve_unique_paths(x - 1, y, dp)
        return dp[x][y]

    def get_num_unique_paths(R, C):
        # Don't use [[None]*C]*R, it's a reference and could mess up the solution
        dp = [[None for _ in range(C)] for _ in range(R)]
        return solve_unique_paths(R - 1, C - 1, dp)

    print(get_num_unique_paths(2, 2))
    print(get_num_unique_paths(2, 3))
    print(get_num_unique_paths(3, 3))


def tabulation():
    def get_num_unique_paths(R, C):
        dp = [[None for _ in range(C)] for _ in range(R)]

        # base condition, the top-left cell will have only 1 number of ways to reach (0, 0).
        dp[0][0] = 1

        # traverse the whole matrix now (reverse direction of the memoized solution).
        for x in range(R):
            for y in range(C):
                # if you're at (0, 0), ensure that dp[0][0] = 1
                if x == 0 and y == 0:
                    dp[x][y] = 1
                else:
                    # else, number of ways at (x, y) would be equal to the
                    # number of ways from upper and left cells. Ensure that you add a 0
                    # in case indices are out of bounds (from the base condition of memoized solution).
                    left = dp[x][y - 1] if y > 0 else 0
                    up = dp[x - 1][y] if x > 0 else 0
                    dp[x][y] = left + up

        # at the end, answer always lies at the destination cell.
        return dp[R - 1][C - 1]

    print(get_num_unique_paths(2, 2))
    print(get_num_unique_paths(2, 3))
    print(get_num_unique_paths(3, 3))


def space_optimized():
    # The idea is to use a previous row array and follow RASTER SCAN on current row.
    # To compute the number of ways at current cell, we need value from upper cell (in previous row)
    # and the value in just the left cell of the current row.
    def get_num_unique_paths(R, C):
        # create a previous row with 0s (representing out of bounds upper cells)
        prev = [0 for _ in range(C)]

        # start traversing the cells in the matrix
        for x in range(R):
            # initialize the current row with 0s
            curr = [0 for _ in range(C)]

            for y in range(C):
                # if at (0, 0), ensure that current row's first element (representing (0, 0))
                # is assigned a value 1.
                if x == 0 and y == 0:
                    curr[0] = 1
                else:
                    # compute the value from just the upper cell (from previous row)
                    up = prev[y]
                    # compute the value of just the left cell from the current row
                    left = curr[y - 1]
                    # add both the values and assign them to current cell, i.e., curr[y]
                    curr[y] = left + up

            # after traversing current row, update prev with curr
            # now the current row becomes previous row for next iteration.
            prev = curr

        # finally, the answer lies in the previous row's last index
        return prev[C - 1]

    print(get_num_unique_paths(2, 2))
    print(get_num_unique_paths(2, 3))
    print(get_num_unique_paths(3, 3))


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
