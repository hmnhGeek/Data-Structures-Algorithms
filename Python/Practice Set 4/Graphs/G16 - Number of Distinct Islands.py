class Solution:
    @staticmethod
    def _dfs(mtx, i, j, n, m, visited, island, bx, by):
        island.append((i - bx, j - by))
        visited[i][j] = True
        neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m, visited)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, visited, island, bx, by)

    @staticmethod
    def get_distinct_islands(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        unique_islands = set()
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1 and not visited[i][j]:
                    island = []
                    Solution._dfs(mtx, i, j, n, m, visited, island, i, j)
                    unique_islands.add(tuple(island))
        return len(unique_islands)

    @staticmethod
    def _get_valid_neighbours(mtx, i, j, n, m, visited):
        neighbours = []
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1 and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1 and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1 and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1 and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        return neighbours


print(
    Solution.get_distinct_islands(
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0]
        ]
    )
)

print(
    Solution.get_distinct_islands(
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]
        ]
    )
)

print(
    Solution.get_distinct_islands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    )
)

print(
    Solution.get_distinct_islands(
        [
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, 1]
        ]
    )
)
