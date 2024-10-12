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
    def _dfs(mtx, i, j, visited, vector, n, m, base_x, base_y):
        visited[i][j] = True
        vector.add((i - base_x, j - base_y))
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, visited, vector, n, m, base_x, base_y)

    @staticmethod
    def get_distinct_islands(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        islands = []
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1 and not visited[i][j]:
                    vector = set()
                    Solution._dfs(mtx, i, j, visited, vector, n, m, i, j)
                    if vector not in islands:
                        islands.append(vector)
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
        [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]
    )
)

print(
    Solution.get_distinct_islands(
        [[1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 1, 1]]
    )
)

print(
    Solution.get_distinct_islands(
        [
            [1, 0],
            [0, 1],
            [1, 1]
        ]
    )
)
