def recursive():
    def solve_maze_obstacle(mtx, x, y, R, C):
        # checking this case before (0,0) check because even the value at (0, 0) can be -1.
        if x >= 0 and y >= 0 and mtx[x][y] == -1:
            return 0
        if x == 0 and y == 0:
            return 1
        if x < 0 or y < 0:
            return 0

        return solve_maze_obstacle(mtx, x, y - 1, R, C) + solve_maze_obstacle(mtx, x - 1, y, R, C)

    def maze_obstacle(mtx):
        R, C = len(mtx), len(mtx[0])
        return solve_maze_obstacle(mtx, R - 1, C - 1, R, C)

    print(maze_obstacle([[0, 0, 0], [0, -1, 0], [0, 0, 0]]))
    print(maze_obstacle([[0, 0], [0, 0]]))
    print(maze_obstacle([[0, -1], [-1, 0]]))


def memoized():
    def solve_maze_obstacle(mtx, x, y, R, C, dp):
        # checking this case before (0,0) check because even the value at (0, 0) can be -1.
        if x >= 0 and y >= 0 and mtx[x][y] == -1:
            return 0
        if x == 0 and y == 0:
            return 1
        if x < 0 or y < 0:
            return 0

        if dp[x][y] is not None:
            return dp[x][y]

        dp[x][y] = solve_maze_obstacle(mtx, x, y - 1, R, C, dp) + solve_maze_obstacle(mtx, x - 1, y, R, C, dp)
        return dp[x][y]

    def maze_obstacle(mtx):
        R, C = len(mtx), len(mtx[0])
        dp = [[None for _ in range(C)] for _ in range(R)]
        return solve_maze_obstacle(mtx, R - 1, C - 1, R, C, dp)

    print(maze_obstacle([[0, 0, 0], [0, -1, 0], [0, 0, 0]]))
    print(maze_obstacle([[0, 0], [0, 0]]))
    print(maze_obstacle([[0, -1], [-1, 0]]))


def tabulation():
    def maze_obstacle(mtx):
        R, C = len(mtx), len(mtx[0])
        dp = [[None for _ in range(C)] for _ in range(R)]

        dp[0][0] = 1 if mtx[0][0] != -1 else 0

        for x in range(R):
            for y in range(C):
                # add a case check for (x, y) cell; if the value is -1, before even checking for (0, 0).
                if mtx[x][y] == -1:
                    dp[x][y] = 0
                elif x == 0 and y == 0:
                    dp[0][0] = 1
                else:
                    up = dp[x - 1][y] if x > 0 else 0
                    left = dp[x][y - 1] if y > 0 else 0
                    dp[x][y] = up + left

        return dp[R - 1][C - 1]

    print(maze_obstacle([[0, 0, 0], [0, -1, 0], [0, 0, 0]]))
    print(maze_obstacle([[0, 0], [0, 0]]))
    print(maze_obstacle([[0, -1], [-1, 0]]))


def space_optimized():
    def maze_obstacle(mtx):
        R, C = len(mtx), len(mtx[0])
        prev = [0 for _ in range(C)]
        prev[0] = 1 if mtx[0][0] != -1 else 0

        for x in range(R):
            curr = [0 for _ in range(C)]
            for y in range(C):
                # add a case check for (x, y) cell; if the value is -1, before even checking for (0, 0).
                if mtx[x][y] == -1:
                    curr[y] = 0
                elif x == 0 and y == 0:
                    curr[0] = 1
                else:
                    up = prev[y]
                    left = curr[y - 1]
                    curr[y] = up + left

            prev = curr

        return prev[C - 1]

    print(maze_obstacle([[0, 0, 0], [0, -1, 0], [0, 0, 0]]))
    print(maze_obstacle([[0, 0], [0, 0]]))
    print(maze_obstacle([[0, -1], [-1, 0]]))


print("Recursion Solution")
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