# Problem link - https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1
# Solution - https://www.youtube.com/watch?v=C-2_uSRli8o&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=9


class Solution:
    @staticmethod
    def _dfs(mtx, i, j, original_color, new_color, n, m):
        # update the color of the (i, j) cell.
        mtx[i][j] = new_color

        # get the neighbours of the cell
        neighbours = Solution._get_neighbours(mtx, i, j, n, m, new_color)

        # perform DFS on the adjacent cells if they satisfy original color validation.
        for neighbour in neighbours:
            x, y = neighbour
            if mtx[x][y] == original_color:
                Solution._dfs(mtx, x, y, original_color, new_color, n, m)

    @staticmethod
    def flood_fill(mtx, new_color, src_x, src_y):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """

        # get the dimensions of the matrix.
        n = len(mtx)
        m = len(mtx[0])

        # check if the source cell is not in the matrix.
        if not (0 <= src_x < n and 0 <= src_y < m):
            return

        # store the original color for DFS reference.
        original_color = mtx[src_x][src_y]

        # start the DFS from the source cell. In worst case it will traverse all the cells and so it is O(mn) operation.
        if mtx[src_x][src_y] == original_color and mtx[src_x][src_y] != new_color:
            Solution._dfs(mtx, src_x, src_y, original_color, new_color, n, m)

        # print the matrix.
        for i in range(n):
            print(mtx[i])
        print()

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m, new_color):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] != new_color:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] != new_color:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] != new_color:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] != new_color:
            neighbours.append((i, j - 1))
        return neighbours


Solution.flood_fill(
    [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ],
    2,
    1,
    1
)

Solution.flood_fill(
    [[0, 0, 0], [0, 0, 0]],
    0, 0, 0
)

Solution.flood_fill(
    [[0, 0, 0], [0, 0, 0]], 0, 0, 0
)

Solution.flood_fill(
    [
        [0, 0, 0],
        [0, 1, 1]
    ],
    1,
    1,
    1
)

Solution.flood_fill(
    [
        [2, 2, 2],
        [2, 2, 2]
    ],
    1,
    0, 0
)