class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, i, j, n, m, bx, by, island, visited):
        visited[i][j] = True
        island.append((bx - i, by - j))
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, bx, by, island, visited)

    @staticmethod
    def get_distinct_islands(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        islands = set()
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1 and not visited[i][j]:
                    island = []
                    Solution._dfs(mtx, i, j, n, m, i, j, island, visited)
                    islands.add(tuple(island))
        return len(islands)


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