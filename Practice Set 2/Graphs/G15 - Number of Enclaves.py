class Solution:
    @staticmethod
    def _get_valid_neighbours(mtx, visited, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1 and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1 and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1 and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1 and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, visited, i, j, n, m):
        visited[i][j] = True
        neighbours = Solution._get_valid_neighbours(mtx, visited, i, j, n, m)
        for neighbour in neighbours:
            Solution._dfs(mtx, visited, neighbour[0], neighbour[1], n, m)

    @staticmethod
    def get_num_enclaves(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        count = 0

        for j in range(m):
            if mtx[0][j] == 1 and not visited[0][j]:
                Solution._dfs(mtx, visited, 0, j, n, m)

        for i in range(n):
            if mtx[i][m - 1] == 1 and not visited[i][m - 1]:
                Solution._dfs(mtx, visited, i, m - 1, n, m)

        for j in range(m):
            if mtx[n - 1][j] == 1 and not visited[n - 1][j]:
                Solution._dfs(mtx, visited, n - 1, j, n, m)

        for i in range(n):
            if mtx[i][0] == 1 and not visited[i][0]:
                Solution._dfs(mtx, visited, i, 0, n, m)

        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1 and not visited[i][j]:
                    count += 1
        return count


print(
    Solution.get_num_enclaves(
        [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    )
)

print(
    Solution.get_num_enclaves(
        [
            [0, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [0, 1, 1, 0]
        ]
    )
)

print(Solution.get_num_enclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
