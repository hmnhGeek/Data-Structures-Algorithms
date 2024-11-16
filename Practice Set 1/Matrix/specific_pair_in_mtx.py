# Problem link - https://www.naukri.com/code360/problems/find-a-specific-pair-in-the-matrix_1115467
# Solution - https://www.youtube.com/watch?v=aUhR_T5J9is&t=1929s


class Solution:
    @staticmethod
    def find_specific_pair(mtx):
        """
            Time complexity is O(n^2) and space complexity is O(n^2).
        """

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