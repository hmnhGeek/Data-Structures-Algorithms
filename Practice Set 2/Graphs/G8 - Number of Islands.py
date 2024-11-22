class Solution:
    @staticmethod
    def _get_valid_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= i - 1 < n and 0 <= j + 1 < m and mtx[i - 1][j + 1]:
            neighbours.append((i - 1, j + 1))
        if 0 <= j + 1 < m and mtx[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and 0 <= j + 1 < m and mtx[i + 1][j + 1]:
            neighbours.append((i + 1, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= i + 1 < n and 0 <= j - 1 < m and mtx[i + 1][j - 1]:
            neighbours.append((i + 1, j - 1))
        if 0 <= j - 1 < m and mtx[i][j - 1]:
            neighbours.append((i, j - 1))
        if 0 <= i - 1 < n and 0 <= j - 1 < m and mtx[i - 1][j - 1]:
            neighbours.append((i - 1, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, i, j, n, m, visited):
        visited[i][j] = True
        neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, visited)

    @staticmethod
    def get_num_islands(mtx):
        n, m = len(mtx), len(mtx[0])
        num_islands = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and mtx[i][j] == 1:
                    num_islands += 1
                    Solution._dfs(mtx, i, j, n, m, visited)
        return num_islands


print(
    Solution.get_num_islands(
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 1]
        ]
    )
)

print(Solution.get_num_islands([[0, 1], [1, 0], [1, 1], [1, 0]]))
print(Solution.get_num_islands([[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]))
print(
    Solution.get_num_islands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
    )
)

print(
    Solution.get_num_islands(
        [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0]]
    )
)

print(
    Solution.get_num_islands(
        [
            [0, 0],
            [0, 0]
        ]
    )
)

print(
    Solution.get_num_islands(
        [
            [1, 1],
            [1, 1]
        ]
    )
)