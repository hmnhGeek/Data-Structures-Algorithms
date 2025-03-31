# Problem link - https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/


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
            # start from `i + 1` cell so that we don't swap the cells two times and get back the same matrix.
            for j in range(i + 1, n):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    @staticmethod
    def _lateral_invert(mtx, n):
        for i in range(n):
            Solution._reverse_arr(mtx, i, n)

    @staticmethod
    def rotate_90_deg_clockwise(mtx):
        """
            Time complexity is O(n^2) and space complexity is O(1).
        """

        n = len(mtx)

        # take the transpose of the matrix in O(n^2) time.
        Solution._transpose(mtx, n)

        # Laterally invert each row of the matrix in O(n^2) time.
        Solution._lateral_invert(mtx, n)

        # print the rotated matrix.
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

Solution.rotate_90_deg_clockwise([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
