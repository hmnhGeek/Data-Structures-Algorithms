class Solution:
    @staticmethod
    def _transpose(mtx):
        n = len(mtx)
        for i in range(n):
            for j in range(i):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    @staticmethod
    def _lateral_invert(mtx):
        n = len(mtx)
        for i in range(n):
            Solution._invert(mtx[i])

    @staticmethod
    def _invert(arr):
        i, j = 0, len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    @staticmethod
    def rotate(mtx):
        Solution._transpose(mtx)
        Solution._lateral_invert(mtx)
        print(mtx)


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
