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


mtx = [[1, 2, -1, -4, -20],
       [-8, -3, 4, 2, 1],
       [3, 8, 6, 1, 3],
       [-4, -1, 1, 7, -6],
       [0, -4, 10, -5, 1]]

print(BiQuadraticSolution.get_specific_pair(mtx))
