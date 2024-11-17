# Problem link - https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/


class Solution:
    @staticmethod
    def _transpose(mtx, n):
        for i in range(n):
            for j in range(i + 1, n):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]
        return mtx

    @staticmethod
    def rotate(mtx):
        n = len(mtx)
        mtx = Solution._transpose(mtx, n)
        for i in range(n):
            mtx[i] = mtx[i][-1:-n-1:-1]
        return mtx


print(
    Solution.rotate(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(
    Solution.rotate(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
    )
)