# Problem link - https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/
# Solution - https://youtube.com/watch?v=aUhR_T5J9is


class BiQuadraticSolution:
    """
        This is a O(n^4) solution with O(1) space.
    """

    @staticmethod
    def get_specific_pair(mtx):
        # store the maximum value in a variable
        max_value = -1e6
        n = len(mtx)
        # loop for each element in the matrix just before the last row and last column
        for a in range(n - 1):
            for b in range(n - 1):
                # loop in the sub matrix from next row and next column till last row and last column
                # we do this because we want c > a and d > b.
                for c in range(a + 1, n):
                    for d in range(b + 1, n):
                        # update the maximum value
                        max_value = max(max_value, mtx[c][d] - mtx[a][b])
        # finally return the maximum value
        return max_value


class QuadraticSolution:
    """
        Overall time complexity is O(n^2) and overall space complexity is O(n^2).
    """

    @staticmethod
    def get_specific_pair(mtx):
        # store the number of rows and columns in a variable (it's a square matrix).
        n = len(mtx)

        # create a blank matrix with exact same dimensions as that of the original matrix. Hence, we now have
        # an additional space of O(n^2).
        max_mtx = [[None for _ in range(n)] for _ in range(n)]
        # initialize the bottom right corner of this matrix to the same value from the original matrix.
        max_mtx[n - 1][n - 1] = mtx[n - 1][n - 1]

        # now fill up the last row and last column of the max-matrix starting from the second last cell. This will take
        # O(n) time.
        for i in range(n - 2, -1, -1):
            # fill the last column with the max of the current cell from matrix and the top cell from the
            # max-matrix's last column.
            max_mtx[i][n - 1] = max(mtx[i][n - 1], max_mtx[i + 1][n - 1])
            # fill the last row with the max of the current cell from matrix and the leftmost cell from the
            # max-matrix's last row.
            max_mtx[n - 1][i] = max(mtx[n - 1][i], max_mtx[n - 1][i + 1])

        # now start filling the other cells in the max-matrix from back direction from second last row and column. This
        # will take O(n^2) time.
        for i in range(n - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                # assign the max_mtx[i][j] = max of mtx[i][j] and top left of both sub matrices.
                max_mtx[i][j] = max(mtx[i][j], max_mtx[i + 1][j], max_mtx[i][j + 1])

        # once the max matrix is filled, initialize a result variable which will store -inf as max value.
        max_value = -1e6
        # loop till second last row and second last column because if will till last, we won't be having any meaning
        # for c, d which are greater than a, b respectively. This will take O(n^2) time.
        for i in range(n - 1):
            for j in range(n - 1):
                # update the max value with the difference from sub-matrix's top left and the current value of the
                # matrix.
                max_value = max(max_value, max_mtx[i + 1][j + 1] - mtx[i][j])
        # return the max value.
        return max_value


class Solution:
    @staticmethod
    def using_bi_quadratic_time(mtx):
        print(BiQuadraticSolution.get_specific_pair(mtx))

    @staticmethod
    def using_quadratic_time(mtx):
        print(QuadraticSolution.get_specific_pair(mtx))


mtx = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 6, 1, 3],
       [-4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1]]

Solution.using_bi_quadratic_time(mtx)
Solution.using_quadratic_time(mtx)