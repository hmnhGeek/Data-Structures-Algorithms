class Solution:
    @staticmethod
    def _dfs(mtx, i, j, original_color, new_color, n, m):
        mtx[i][j] = new_color
        neighbours = Solution._get_neighbours(mtx, i, j, n, m, new_color)
        for neighbour in neighbours:
            x, y = neighbour
            if mtx[x][y] == original_color:
                Solution._dfs(mtx, x, y, original_color, new_color, n, m)

    @staticmethod
    def flood_fill(mtx, new_color, src_x, src_y):
        n = len(mtx)
        m = len(mtx[0])
        if not (0 <= src_x < n and 0 <= src_y < m):
            return
        original_color = mtx[src_x][src_y]
        if mtx[src_x][src_y] == original_color and mtx[src_x][src_y] != new_color:
            Solution._dfs(mtx, src_x, src_y, original_color, new_color, n, m)
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