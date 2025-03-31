# Problem link - https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1
# Solution - https://www.youtube.com/watch?v=7zmgQSJghpo&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=16


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
        # mark this cell as visited and convert (i, j) to normalized cell before adding into vector
        visited[i][j] = True
        vector.append((i - base_x, j - base_y))

        # get the neighbours of this cell in the order U-R-D-L.
        neighbours = Solution._get_neighbours(mtx, i, j, n, m)

        # loop on the neighbour cells of this cell.
        for neighbour in neighbours:
            x, y = neighbour
            # if the neighbour cell is not visited, make a recursive DFS call with the adjacent cell coordinate.
            if not visited[x][y]:
                Solution._dfs(mtx, x, y, visited, vector, n, m, base_x, base_y)

    @staticmethod
    def get_distinct_islands(mtx):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """

        # store the dimensions of the matrix
        n, m = len(mtx), len(mtx[0])
        # create a blank visited matrix which will take O(m*n) space.
        visited = [[False for _ in range(m)] for _ in range(n)]
        # create a blank set to store the unique islands in the matrix.
        islands = set()

        # raster scan in the matrix
        for i in range(n):
            for j in range(m):
                # if the current cell is a 1 and is not visited, we have found a new component; let's do a DFS
                # traversal starting from this cell.
                if mtx[i][j] == 1 and not visited[i][j]:
                    # create a blank list to store the cells of the island in this order: U-R-D-L
                    vector = []
                    # call the DFS method with last two parameters for the starting cell of this component which will
                    # now act as base cell coordinates for recursive DFS calls for this component.
                    Solution._dfs(mtx, i, j, visited, vector, n, m, i, j)
                    # convert the list `vector` into tuple and add it into the islands set
                    islands.add(tuple(vector))
        # return the count of unique islands
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
