# Problem link - https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

def get_all_paths(mtx, i, j, path, paths, visited, n):
    # if rat is at the last cell, there exists a path, append path into the paths list.
    if i == n - 1 and j == n - 1:
        paths.append(path)

    # mark this cell as visited.
    visited[i][j] = True

    # move the rat in downward direction if there exists a cell below which is not visited.
    if 0 <= i + 1 < n and mtx[i + 1][j] == 1 and not visited[i + 1][j]:
        get_all_paths(mtx, i + 1, j, path + 'D', paths, visited, n)

    # move the rat in left direction if there exists a cell at left which is not visited.
    if 0 <= j - 1 < n and mtx[i][j - 1] == 1 and not visited[i][j - 1]:
        get_all_paths(mtx, i, j - 1, path + 'L', paths, visited, n)

    # move the rat in right direction if there exists a cell at right which is not visited.
    if 0 <= j + 1 < n and mtx[i][j + 1] == 1 and not visited[i][j + 1]:
        get_all_paths(mtx, i, j + 1, path + 'R', paths, visited, n)

    # move the rat in upward direction if there exists a cell up which is not visited.
    if 0 <= i - 1 < n and mtx[i - 1][j] == 1 and not visited[i - 1][j]:
        get_all_paths(mtx, i - 1, j, path + 'U', paths, visited, n)

    # backtrack to this cell by unmarking it as visited.
    visited[i][j] = False


def rat_in_a_maze(mtx, n):
    # if the starting cell is 0 and last cell is 0, return a blank array
    # as there will be no path from start to end.
    if mtx[0][0] == 0 or mtx[n - 1][n - 1] == 0:
        return []

    # initialize a paths list which will store all the paths which the rat can travel.
    paths = []

    # initialize a visited array
    visited = [[False for _ in range(n)] for _ in range(n)]

    # call the backtracking function to fill up the paths array.
    get_all_paths(mtx, 0, 0, '', paths, visited, n)

    # once the paths array is updated, return it.
    return paths


print(
    rat_in_a_maze(
    [
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]
        ], 4
    )
)

print(
    rat_in_a_maze(
    [
            [1, 0],
            [1, 0]
        ], 2
    )
)