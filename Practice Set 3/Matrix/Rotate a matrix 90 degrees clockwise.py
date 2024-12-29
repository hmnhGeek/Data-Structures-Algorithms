class Solution:
    @staticmethod
    def _reverse_arr(mtx, i, n):
        x, y = 0, n - 1
        while x < y:
            mtx[i][x], mtx[i][y] = mtx[i][y], mtx[i][x]
            x += 1
            y -= 1

    @staticmethod
    def _transpose(mtx, n):
        for i in range(n):
            for j in range(i + 1, n):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    @staticmethod
    def _lateral_invert(mtx, n):
        for i in range(n):
            Solution._reverse_arr(mtx, i, n)

    @staticmethod
    def rotate_90_deg_clockwise(mtx):
        n = len(mtx)
        Solution._transpose(mtx, n)
        Solution._lateral_invert(mtx, n)
        for i in range(n):
            print(mtx[i])
        print()


Solution.rotate_90_deg_clockwise(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

Solution.rotate_90_deg_clockwise(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
)
