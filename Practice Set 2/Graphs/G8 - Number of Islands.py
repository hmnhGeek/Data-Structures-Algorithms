# Problem link - https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1
# Solution - https://www.youtube.com/watch?v=muncqlKJrH0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=8


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
        # mark the current cell as visited
        visited[i][j] = True
        # get all non-zero neighbouring cells of cell (i, j) from 8 directions in O(1) time.
        neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m)
        # perform DFS on those neighbours which are not visited.
        for neighbour in neighbours:
            x, y = neighbour
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, n, m, visited)

    @staticmethod
    def get_num_islands(mtx):
        """
            Overall time complexity is O(n*m) and space complexity is O(n*m) for visited matrix.
        """

        # get the dimensions of the matrix
        n, m = len(mtx), len(mtx[0])
        # store the count of the islands as 0.
        num_islands = 0
        # create a visited matrix.
        visited = [[False for _ in range(m)] for _ in range(n)]
        # loop on the matrix in O(n*m).
        for i in range(n):
            for j in range(m):
                # if the current cell is 1 and is not visited, we have found a starting cell for an island.
                if not visited[i][j] and mtx[i][j] == 1:
                    # increment the count of founded islands.
                    num_islands += 1
                    # perform DFS on (i, j) cell.
                    Solution._dfs(mtx, i, j, n, m, visited)
        # return the number of islands.
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