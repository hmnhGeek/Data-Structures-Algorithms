# Problem link - https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/


class Solution:
    @staticmethod
    def rotate_90_deg_clockwise(mtx):
        """
            Time complexity is O(n^2) and space complexity is O(1).
        """
        n = len(mtx)
        Solution._transpose(mtx, n)
        Solution._lateral_invert(mtx, n)
        for i in range(n):
            print(mtx[i])
        print()

    @staticmethod
    def _transpose(mtx, n):
        for i in range(n):
            for j in range(i + 1, n):
                temp = mtx[i][j]
                mtx[i][j] = mtx[j][i]
                mtx[j][i] = temp

    @staticmethod
    def _reverse(arr, n):
        i, j = 0, n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    @staticmethod
    def _lateral_invert(mtx, n):
        for i in range(n):
            Solution._reverse(mtx[i], n)


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
