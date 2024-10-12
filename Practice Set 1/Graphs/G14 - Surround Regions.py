class Solution:
    @staticmethod
    def show(mtx):
        for i in mtx:
            print(i)
        print()

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 0:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 0:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, x, y, visited, n, m):
        visited[x][y] = True
        mtx[x][y] = 2
        neighbours = Solution._get_neighbours(mtx, x, y, n, m)
        for neighbour in neighbours:
            x0, y0 = neighbour
            if not visited[x0][y0]:
                Solution._dfs(mtx, x0, y0, visited, n, m)

    @staticmethod
    def surround_regions(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        # cover first row
        for j in range(m):
            if mtx[0][j] == 0:
                Solution._dfs(mtx, 0, j, visited, n, m)

        # cover last column
        for i in range(n):
            if mtx[i][m - 1] == 0:
                Solution._dfs(mtx, i, m - 1, visited, n, m)

        # cover last row
        for j in range(m):
            if mtx[n - 1][j] == 0:
                Solution._dfs(mtx, n - 1, j, visited, n, m)

        # cover first column
        for i in range(n):
            if mtx[i][0] == 0:
                Solution._dfs(mtx, i, 0, visited, n, m)

        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 0:
                    mtx[i][j] = 1
                elif mtx[i][j] == 2:
                    mtx[i][j] = 0

        Solution.show(mtx)


Solution.surround_regions(
    [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0]
    ]
)

Solution.surround_regions(
    [
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0]
    ]
)

Solution.surround_regions(
    [[1, 0, 1, 1, 1, 1],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 0]]
)

Solution.surround_regions(
    [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1]
    ]
)

Solution.surround_regions(
    [[1]]
)