# Problem link - https://leetcode.com/problems/number-of-enclaves/description/
# Solution - https://www.youtube.com/watch?v=rxKcepXQgU4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=15


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
    def _dfs(mtx, i, j, n, m, visited):
        visited[i][j] = True
        mtx[i][j] = 2
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)

        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, visited)

    @staticmethod
    def num_enclaves(mtx):
        """
            The approach is similar to the G14 problem. The only difference here is that we first convert the bordered
            components of 1 values to 2s and then count the middle 1s and finally convert back the 2s to 1s.

            Time complexity is O(n*m) and space complexity is O(n*m).
        """
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        # traverse the first row
        for j in range(m):
            if mtx[0][j] == 1:
                Solution._dfs(mtx, 0, j, n, m, visited)

        # traverse the last column
        for i in range(n):
            if mtx[i][m - 1] == 1:
                Solution._dfs(mtx, i, m - 1, n, m, visited)

        # traverse the last row
        for j in range(m):
            if mtx[n - 1][j] == 1:
                Solution._dfs(mtx, n - 1, j, n, m, visited)

        # traverse the first column
        for i in range(n):
            if mtx[i][0] == 1:
                Solution._dfs(mtx, i, 0, n, m, visited)

        count1s = 0
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 1:
                    count1s += 1

        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 2:
                    mtx[i][j] = 1

        print(count1s)


Solution.num_enclaves(
    [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]]
)

Solution.num_enclaves(
    [[0, 0, 0, 1],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 1],
     [0, 1, 1, 0]]
)

Solution.num_enclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
