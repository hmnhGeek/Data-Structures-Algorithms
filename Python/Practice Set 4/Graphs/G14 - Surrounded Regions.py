class Solution:
    @staticmethod
    def surround_regions(mtx):
        n, m = len(mtx), len(mtx[0])
        for j in range(m - 1):
            if mtx[0][j] == 'O':
                Solution._dfs(mtx, 0, j, n, m)
        for i in range(n - 1):
            if mtx[i][m - 1] == 'O':
                Solution._dfs(mtx, i, m - 1, n, m)
        for j in range(m - 1, 0, -1):
            if mtx[n - 1][j] == 'O':
                Solution._dfs(mtx, n - 1, j, n, m)
        for i in range(n - 1, 0, -1):
            if mtx[i][0] == 'O':
                Solution._dfs(mtx, i, 0, n, m)
        Solution.convert_os_to_xs(mtx, n, m)
        Solution.convert_zs_to_os(mtx, n, m)
        for i in range(n):
            print(mtx[i])
        print()

    @staticmethod
    def _dfs(mtx, i, j, n, m):
        mtx[i][j] = 'Z'
        neighbours = Solution._get_valid_neighbours(mtx, i, j, n, m)
        for neighbour in neighbours:
            x, y = neighbour
            Solution._dfs(mtx, x, y, n, m)

    @staticmethod
    def _get_valid_neighbours(mtx, i, j, n, m):
        result = []
        if n > i - 1 >= 0 and mtx[i - 1][j] == 'O':
            result.append((i - 1, j))
        if m > j + 1 >= 0 and mtx[i][j + 1] == 'O':
            result.append((i, j + 1))
        if n > i + 1 >= 0 and mtx[i + 1][j] == 'O':
            result.append((i + 1, j))
        if m > j - 1 >= 0 and mtx[i][j - 1] == 'O':
            result.append((i, j - 1))
        return result

    @staticmethod
    def convert_os_to_xs(mtx, n, m):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 'O':
                    mtx[i][j] = 'X'

    @staticmethod
    def convert_zs_to_os(mtx, n, m):
        for i in range(n):
            for j in range(m):
                if mtx[i][j] == 'Z':
                    mtx[i][j] = 'O'



Solution.surround_regions(
    [['X', 'X', 'X', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'X', 'O', 'O']]
)

Solution.surround_regions(
    [['X', 'O', 'X', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'O', 'X', 'X'],
     ['X', 'X', 'O', 'O']]
)

Solution.surround_regions(
    [['X', 'X', 'X'],
     ['X', 'O', 'X'],
     ['X', 'X', 'X']]
)

Solution.surround_regions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])

Solution.surround_regions([["X"]])