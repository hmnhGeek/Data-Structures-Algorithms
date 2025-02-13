class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m, visited):
        neighbours = []
        if 0 <= i - 1 < n and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _solve(mtx, i, j, max_path_effort, min_effort, visited, n, m):
        if i == 0 and j == 0:
            min_effort[0] = min(min_effort[0], max_path_effort)
            return

        # mark the current cell as path visited.
        visited[i][j] = True

        # get the neighbours in constant time.
        neighbours = Solution._get_neighbours(mtx, i, j, n, m, visited)

        # loop on the neighbours
        for neighbour in neighbours:
            x, y = neighbour[0], neighbour[1]
            # recursively find the max path effort
            Solution._solve(mtx, x, y, max(max_path_effort, abs(mtx[i][j] - mtx[x][y])), min_effort, visited, n, m)

        # while returning, unmark the cell from path visited.
        visited[i][j] = False
        return

    @staticmethod
    def get_min_effort(mtx):
        n, m = len(mtx), len(mtx[0])

        # This will take O(mn) space.
        visited = [[False for _ in range(m)] for _ in range(n)]

        # store the global min effort as reference.
        min_effort = [1e6,]

        # start traversals from the last cell.
        Solution._solve(mtx, n - 1, m - 1, -1e6, min_effort, visited, n, m)

        # return the min effort.
        return min_effort[0]


print(
    Solution.get_min_effort(
        [
            [1, 2, 2],
            [3, 8, 2],
            [5, 3, 5]
        ]
    )
)

print(Solution.get_min_effort([[7, 7], [7, 7]]))
print(Solution.get_min_effort([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
print(Solution.get_min_effort([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))
print(Solution.get_min_effort([[1, 8, 8], [3, 8, 9], [5, 3, 5]]))
print(Solution.get_min_effort(
    [
        [1, 3, 1],
        [9, 9, 3],
        [9, 9, 1]
    ]
))
