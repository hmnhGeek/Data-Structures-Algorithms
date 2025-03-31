# Problem link - https://www.geeksforgeeks.org/problems/replace-os-with-xs0052/1
# Solution - https://www.youtube.com/watch?v=BtdgAys4yMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=14


class Solution:
    @staticmethod
    def _get_valid_neighbours(mtx, i, j, n, m, visited):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 0 and not visited[i - 1][j]:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 0 and not visited[i][j + 1]:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 0 and not visited[i + 1][j]:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 0 and not visited[i][j - 1]:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, i, j, n, m, visited):
        visited[i][j] = True
        neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m, visited)
        for neighbour in neighbours:
            Solution._dfs(mtx, neighbour[0], neighbour[1], n, m, visited)

    @staticmethod
    def surround_regions(mtx):
        """
            Time complexity is O(n * m) and space complexity is O(n * m)
        """
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        # Visit all the 0s which are attached to any boundary through any linkage.

        for j in range(m):
            if mtx[0][j] == 0 and not visited[0][j]:
                Solution._dfs(mtx, 0, j, n, m, visited)

        for i in range(n):
            if mtx[i][m - 1] == 0 and not visited[i][m - 1]:
                Solution._dfs(mtx, i, m - 1, n, m, visited)

        for j in range(m):
            if mtx[n - 1][j] == 0 and not visited[n - 1][j]:
                Solution._dfs(mtx, n - 1, j, n, m, visited)

        for i in range(n):
            if mtx[i][0] == 0 and not visited[i][0]:
                Solution._dfs(mtx, i, 0, n, m, visited)

        # once this is done, traverse on n and m
        for i in range(n):
            for j in range(m):
                # if the current cell is a 0, and it is not visited, then it must not be attached from any boundary,
                # set that 0 to a 1 as per the problem.
                if mtx[i][j] == 0 and not visited[i][j]:
                    mtx[i][j] = 1

        for i in mtx:
            print(i)
        print()


Solution.surround_regions(
    [
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0]
    ]
)

Solution.surround_regions(
    [
        [1, 0, 1, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0]
    ]
)

Solution.surround_regions(
    [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1]
    ]
)

Solution.surround_regions([[1]])

Solution.surround_regions(
    [
        [1, 1, 0, 0],
        [1, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]
    ]
)

Solution.surround_regions(
    [
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 0]
    ]
)