class Solution:
    @staticmethod
    def rotate(mtx):
        n, m = len(mtx), len(mtx[0])
        Solution._transpose(mtx, n, m)
        Solution._lateral_invert(mtx, n, m)
        for row in mtx:
            print(row)
        print()

    @staticmethod
    def _transpose(mtx, n, m):
        for i in range(n):
            for j in range(i, n):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    @staticmethod
    def _lateral_invert(mtx, n, m):
        for i in range(n):
            Solution._reverse(mtx, i, m)

    @staticmethod
    def _reverse(mtx, i, m):
        l, h = 0, m - 1
        while l < h:
            mtx[i][l], mtx[i][h] = mtx[i][h], mtx[i][l]
            l += 1
            h -= 1


Solution.rotate(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

Solution.rotate(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
)
