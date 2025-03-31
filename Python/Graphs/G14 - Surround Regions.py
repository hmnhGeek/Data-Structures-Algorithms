# Problem link - https://leetcode.com/problems/surrounded-regions/description/
# Solution - https://www.youtube.com/watch?v=BtdgAys4yMk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=14


class Solution:
    @staticmethod
    def show(mtx):
        for i in mtx:
            print(i)
        print()

    @staticmethod
    def _get_neighbours(mtx, i, j, n, m):
        neighbours = []
        if 0 <= i - 1 < n and mtx[i - 1][j] == 0:
            neighbours.append((i - 1, j))
        if 0 <= j + 1 < m and mtx[i][j + 1] == 0:
            neighbours.append((i, j + 1))
        if 0 <= i + 1 < n and mtx[i + 1][j] == 0:
            neighbours.append((i + 1, j))
        if 0 <= j - 1 < m and mtx[i][j - 1] == 0:
            neighbours.append((i, j - 1))
        return neighbours

    @staticmethod
    def _dfs(mtx, x, y, visited, n, m):
        # mark the current node as visited and set its value in the original matrix to 2.
        visited[x][y] = True
        mtx[x][y] = 2

        # get the neighbours of the current node.
        neighbours = Solution._get_neighbours(mtx, x, y, n, m)

        # DFS traversal on the adjacent nodes.
        for neighbour in neighbours:
            x0, y0 = neighbour
            if not visited[x0][y0]:
                Solution._dfs(mtx, x0, y0, visited, n, m)

    @staticmethod
    def surround_regions(mtx):
        """
            Overall time complexity is O(n*m) and space complexity is also O(n*m).
        """

        # extract the dimensions of the matrix
        n, m = len(mtx), len(mtx[0])
        # create a blank visited matrix
        visited = [[False for _ in range(m)] for _ in range(n)]

        # The idea is to traverse on the outer boundary of the matrix. Wherever there is a zero on the boundary, we
        # initiate a DFS traversal and during the traversal convert all the zeros to 2s. Once the boundary traversal is
        # completed, we traverse on the matrix again. This time, since the inner 0s will be un-touched, we convert them
        # to 1s and the 2s back to 0s (because boundary 0s and all those 0s attached to them should remain intact).

        # cover first row
        for j in range(m):
            if mtx[0][j] == 0:
                Solution._dfs(mtx, 0, j, visited, n, m)

        # cover last column
        for i in range(n):
            if mtx[i][m - 1] == 0:
                Solution._dfs(mtx, i, m - 1, visited, n, m)

        # cover last row
        for j in range(m):
            if mtx[n - 1][j] == 0:
                Solution._dfs(mtx, n - 1, j, visited, n, m)

        # cover first column
        for i in range(n):
            if mtx[i][0] == 0:
                Solution._dfs(mtx, i, 0, visited, n, m)

        # This will take O(n*m) time.
        for i in range(n):
            for j in range(m):
                # This must be an inner 0, convert it to 1 as per problem requirement.
                if mtx[i][j] == 0:
                    mtx[i][j] = 1
                # this must be a border attached 0 which was converted to 2. Convert it back to 0.
                elif mtx[i][j] == 2:
                    mtx[i][j] = 0

        # finally print the matrix back
        Solution.show(mtx)


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
    [[1, 0, 1, 1, 1, 1],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 0],
     [0, 0, 1, 0, 0, 0]]
)

Solution.surround_regions(
    [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1]
    ]
)

Solution.surround_regions(
    [[1]]
)