# Problem link - https://www.naukri.com/code360/problems/distinct-islands_630460
# Solution - https://www.youtube.com/watch?v=7zmgQSJghpo&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=16


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
        # visit the node.
        visited[i][j] = True
        # add the normalized cell for (i, j) wrt base.
        hash_set.add((base[0] - i, base[1] - j))

        # standard DFS procedure...
        neighbours = Solution._get_valid_neighbours(mtx, visited, i, j, n, m)
        for neighbour in neighbours:
            Solution._dfs(mtx, visited, neighbour[0], neighbour[1], n, m, hash_set, base)

    @staticmethod
    def num_distinct_islands(mtx):
        """
            Time complexity is O(mn) and space complexity is O(mn).
        """

        # store variables for DFS
        n, m = len(mtx), len(mtx[0])
        visited = [[False for _ in range(m)] for _ in range(m)]

        # store distinct islands in this variable.
        islands = []

        # loop on the matrix
        for i in range(n):
            for j in range(m):
                # if a starting node is encountered
                if mtx[i][j] == 1 and not visited[i][j]:
                    # get the traversal vector using DFS
                    traversal = set()
                    Solution._dfs(mtx, visited, i, j, n, m, traversal, (i, j))

                    # if the traversal vector is not in islands, add it into it.
                    if traversal not in islands:
                        islands.append(traversal)

        # return the number of distinct islands.
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
