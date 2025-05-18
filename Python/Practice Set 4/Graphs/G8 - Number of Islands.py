class Solution:
    @staticmethod
    def _dfs(mtx, i, j, visited, n, m):
        visited[i][j] = True
        neighbours = Solution._get_neighbours(mtx, i, j, visited, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, visited, n, m)

    @staticmethod
    def _get_neighbours(mtx, i, j, visited, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 1:
            neighbours.append((i - 1, j))
        if 0 <= i - 1 < n and 0 <= j + 1 < m and mtx[i - 1][j + 1] == 1:
            neighbours.append((i - 1, j + 1))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 1:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and 0 <= j + 1 < m and mtx[i + 1][j + 1] == 1:
            neighbours.append((i + 1, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 1:
            neighbours.append((i + 1, j))
        if 0 <= i + 1 < n and 0 <= j - 1 < m and mtx[i + 1][j - 1] == 1:
            neighbours.append((i + 1, j - 1))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 1:
            neighbours.append((i, j - 1))
        if 0 <= i - 1 < n and 0 <= j - 1 < m and mtx[i - 1][j - 1] == 1:
            neighbours.append((i - 1, j - 1))
        return neighbours

    @staticmethod
    def get_number_of_islands(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        num_components = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and mtx[i][j] == 1:
                    num_components += 1
                    Solution._dfs(mtx, i, j, visited, n, m)
        return num_components


print(
    Solution.get_number_of_islands(
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 1]
        ]
    )
)

print(Solution.get_number_of_islands([[0, 1], [1, 0], [1, 1], [1, 0]]))
print(Solution.get_number_of_islands([[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0]]))
print(
    Solution.get_number_of_islands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
    )
)

print(
    Solution.get_number_of_islands(
        [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0]]
    )
)

print(
    Solution.get_number_of_islands(
        [
            [0, 0],
            [0, 0]
        ]
    )
)

print(
    Solution.get_number_of_islands(
        [
            [1, 1],
            [1, 1]
        ]
    )
)
