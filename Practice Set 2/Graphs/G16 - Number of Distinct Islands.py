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
    def _dfs(mtx, visited, i, j, n, m, hash_set, base):
        visited[i][j] = True
        hash_set.add((base[0] - i, base[1] - j))
        neighbours = Solution._get_valid_neighbours(mtx, visited, i, j, n, m)
        for neighbour in neighbours:
            Solution._dfs(mtx, visited, neighbour[0], neighbour[1], n, m, hash_set, base)

    @staticmethod
    def num_distinct_islands(mtx):
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(m)]
        islands = []
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1 and not visited[i][j]:
                    traversal = set()
                    Solution._dfs(mtx, visited, i, j, n, m, traversal, (i, j))
                    if traversal not in islands:
                        islands.append(traversal)
        return len(islands)


print(
    Solution.num_distinct_islands(
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0]
        ]
    )
)

print(
    Solution.num_distinct_islands(
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]
        ]
    )
)

print(
    Solution.num_distinct_islands(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    )
)

print(
    Solution.num_distinct_islands(
        [
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, 1]
        ]
    )
)
