# Problem link - https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/
# Solution - https://www.youtube.com/watch?v=aUhR_T5J9is&t=1771s


class Solution:
    @staticmethod
    def find_specific_pair(mtx):
        """
            Time complexity is O(nm) and space complexity is O(nm).
        """

        # get the dimensions of the matrix.
        n, m = len(mtx), len(mtx[0])

        # define a max matrix and set the value of right-bottom most cell as mtx value of that cell.
        # This will take O(nm) space.
        max_mtx = [[None for _ in range(m)] for _ in range(n)]
        max_mtx[n - 1][m - 1] = mtx[n - 1][m - 1]

        # populate the last column of the max matrix in O(n) time.
        for i in range(n - 2, -1, -1):
            max_mtx[i][m - 1] = max(max_mtx[i + 1][m - 1], mtx[i][m - 1])

        # populate the last row of the max matrix in O(m) time.
        for j in range(m - 2, -1, -1):
            max_mtx[n - 1][j] = max(max_mtx[n - 1][j + 1], mtx[n - 1][j])

        # populate the rest of the max matrix in O(nm) time.
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                max_mtx[i][j] = max(
                    max_mtx[i + 1][j],
                    max_mtx[i][j + 1],
                    mtx[i][j]
                )

        # get the max difference in another O(nm) time.
        result = -1e6
        for i in range(n - 1):
            for j in range(m - 1):
                result = max(result, max_mtx[i + 1][j + 1] - mtx[i][j])
        print(result)


Solution.find_specific_pair(
    [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 6, 1, 3],
        [-4, -1, 1, 7, -6],
        [0, -4, 10, -5, 1]
    ]
)

Solution.find_specific_pair(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

Solution.find_specific_pair(
    [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
)

Solution.find_specific_pair(
    [
        [1, 5],
        [4, 2]
    ]
)

Solution.find_specific_pair(
    [
        [-1, 5, -3],
        [-14, -5, -2],
        [-7, 8, -9]
    ]
)