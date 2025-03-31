# Problem link - https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/


class Solution:
    @staticmethod
    def _transpose(mtx, n, m):
        for i in range(n):
            for j in range(i + 1, m):
                mtx[i][j], mtx[j][i] = mtx[j][i], mtx[i][j]

    @staticmethod
    def _reverse(mtx, i, m):
        row = mtx[i]
        left, right = 0, m - 1
        while left <= right:
            mtx[i][left], mtx[i][right] = mtx[i][right], mtx[i][left]
            left += 1
            right -= 1

    @staticmethod
    def _lateral_invert(mtx, n, m):
        for i in range(n):
            Solution._reverse(mtx, i, m)

    @staticmethod
    def rotate(mtx):
        """
            Time complexity is O(mn) and space complexity is O(1).
        """
        n, m = len(mtx), len(mtx[0])
        Solution._transpose(mtx, n, m)
        Solution._lateral_invert(mtx, n, m)
        for i in range(n):
            print(mtx[i])
        print()


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
