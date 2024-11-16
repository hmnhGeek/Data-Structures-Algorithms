class Solution:
    @staticmethod
    def find_specific_pair(mtx):
        n = len(mtx)
        max_mtx = [[-1e6 for _ in range(n)] for _ in range(n)]
        max_mtx[n - 1][n - 1] = mtx[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            max_mtx[i][n - 1] = max(mtx[i][n - 1], max_mtx[i + 1][n - 1])
        for j in range(n - 2, -1, -1):
            max_mtx[n - 1][j] = max(mtx[n - 1][j], max_mtx[n - 1][j + 1])
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                max_mtx[i][j] = max(
                    mtx[i][j],
                    max_mtx[i + 1][j],
                    max_mtx[i][j + 1]
                )
        max_output = -1e6
        for i in range(n - 1):
            for j in range(n - 1):
                max_output = max(max_output, max_mtx[i + 1][j + 1] - mtx[i][j])
        print(max_output)


Solution.find_specific_pair(
    [
        [1, 2, -1, -4, 20],
        [-8, -3, 4, 2, 1],
        [3, 8, 6, 1, 3],
        [-4, -1, 1, 7, -6],
        [0, -4, 10, -5, 1]
    ]
)