# Problem link - https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1
# Solution - https://www.youtube.com/watch?v=muncqlKJrH0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=8


class Solution:
    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
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
    def _dfs(mtx, i, j, visited, n, m):
        # mark the cell node as visited.
        visited[i][j] = True

        # get the neighbours of the node in O(1) time and O(8) = O(1) space.
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)

        # loop on the neighbours and start a DFS if not visited.
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, visited, n, m)

    @staticmethod
    def get_number_of_islands(mtx):
        """
            Time complexity is O(nm) and space complexity is O(nm).
        """

        # get the dimensions of the matrix.
        n, m = len(mtx), len(mtx[0])

        # create a visited matrix
        visited = [[False for _ in range(m)] for _ in range(n)]

        # num_islands variable set to 0.
        num_islands = 0

        # loop in the matrix now.
        for i in range(n):
            for j in range(m):
                # if the cell is 1 and not visited, a new component has been found.
                if mtx[i][j] == 1 and not visited[i][j]:
                    num_islands += 1
                    # start a DFS.
                    Solution._dfs(mtx, i, j, visited, n, m)

        # return the number of islands
        return num_islands


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
