class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] != 0:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] != 0:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] != 0:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] != 0:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, i, j, visited, new_color, n, m):
        visited[i][j] = True
        original_color = mtx[i][j]
        mtx[i][j] = new_color
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            if (mtx[x][y] == original_color or mtx[x][y] == new_color) and not visited[x][y]:
                Solution._dfs(mtx, x, y, visited, new_color, n, m)

    @staticmethod
    def flood_fill(mtx, new_color, source_x, source_y):
        n, m = len(mtx), len(mtx[0])
        if source_x < 0 or source_x >= n:
            return
        if source_y < 0 or source_y >= m:
            return
        visited = [[False for _ in range(m)] for _ in range(n)]
        Solution._dfs(mtx, source_x, source_y, visited, new_color, n, m)
        for i in range(n):
            print(mtx[i])
        print()


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