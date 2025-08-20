class Solution:
    @staticmethod
    def get_number_of_enclaves(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        for j in range(m - 1):
            if not visited[0][j] and mtx[0][j] == 1:
                Solution._dfs(mtx, 0, j, n, m, visited)
        for i in range(n - 1):
            if not visited[i][m - 1] and mtx[i][m - 1] == 1:
                Solution._dfs(mtx, i, m - 1, n, m, visited)
        for j in range(m - 1, 0, -1):
            if not visited[n - 1][j] and mtx[n - 1][j] == 1:
                Solution._dfs(mtx, n - 1, j, n, m, visited)
        for i in range(n - 1, 0, -1):
            if not visited[i][0] and mtx[i][0] == 1:
                Solution._dfs(mtx, i, 0, n, m, visited)
        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and mtx[i][j] == 1:
                    count += 1
        return count

    @staticmethod
    def _dfs(mtx, i, j, n, m, visited):
        visited[i][j] = True
        neighbours = Solution._get_neighbours(mtx, i, j, n, m, visited)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, visited)

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m, visited):
        result = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1 and not visited[i - 1][j]:
            result.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1 and not visited[i][j + 1]:
            result.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1 and not visited[i + 1][j]:
            result.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1 and not visited[i][j - 1]:
            result.append((i, j - 1))
        return result


print(
    Solution.get_number_of_enclaves(
        [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    )
)
