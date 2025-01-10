class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == "O":
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == "O":
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == "O":
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == "O":
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, i, j, n, m, visited):
        visited[i][j] = True
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, visited)

    @staticmethod
    def surround_regions(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if mtx[i][0] == "O":
                Solution._dfs(mtx, i, 0, n, m, visited)
        for i in range(n):
            if mtx[i][m - 1] == "O":
                Solution._dfs(mtx, i, m - 1, n, m, visited)
        for j in range(m):
            if mtx[0][j] == "O":
                Solution._dfs(mtx, 0, j, n, m, visited)
        for j in range(m):
            if mtx[n - 1][j] == "O":
                Solution._dfs(mtx, n - 1, j, n, m, visited)
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == "O" and not visited[i][j]:
                    mtx[i][j] = "X"
        for i in range(n):
            print(mtx[i])
        print()


Solution.surround_regions(
    [['X', 'X', 'X', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'X', 'O', 'O']]
)

Solution.surround_regions(
    [['X', 'O', 'X', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'X', 'O', 'O']]
)

Solution.surround_regions(
    [['X', 'X', 'X'],
     ['X', 'O', 'X'],
     ['X', 'X', 'X']]
)

Solution.surround_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])

Solution.surround_regions([["X"]])
