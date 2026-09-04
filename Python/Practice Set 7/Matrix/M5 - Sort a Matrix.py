class Solution:
    @staticmethod
    def sort_matrix(mtx):
        n, m = len(mtx), len(mtx[0])
        flattened_mtx = Solution._flatten(mtx, n, m)
        flattened_mtx.sort()
        return Solution._reconstruct(flattened_mtx, n, m)

    @staticmethod
    def _flatten(mtx, n, m):
        flattened = []
        for i in range(n):
            for j in range(m):
                flattened.append(mtx[i][j])
        return flattened

    @staticmethod
    def _reconstruct(flattened, n, m):
        mtx = []
        i = 0
        while i < n:
            j = 0
            row = []
            while j < m:
                row.append(flattened[(i * m) + j])
                j += 1
            i += 1
            mtx.append(row)
        return mtx


print(Solution.sort_matrix(
    [[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50]]
))

print(Solution.sort_matrix([[1, 5, 3], [2, 8, 7], [4, 6, 9]]))