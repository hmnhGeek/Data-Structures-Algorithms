# Problem link - https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1


class Matrix:
    RIGHT = "R"
    LEFT = "L"
    UP = "U"
    DOWN = "D"

    @staticmethod
    def spiral_traverse(mtx):
        """
            Overall time complexity is O(nm) and space complexity is O(nm).
        """

        n, m = len(mtx), len(mtx[0])

        # initialize pointers to left, right, up and down corners of the matrix.
        left, right, up, down = 0, m - 1, 0, n - 1

        # set the initial traversal direction as right.
        direction = Matrix.RIGHT
        traversal = []

        while left <= right and up <= down:
            if direction == Matrix.RIGHT:
                for i in range(left, right + 1):
                    traversal.append(mtx[up][i])
                up += 1
                direction = Matrix.DOWN
            elif direction == Matrix.DOWN:
                for j in range(up, down + 1):
                    traversal.append(mtx[j][right])
                right -= 1
                direction = Matrix.LEFT
            elif direction == Matrix.LEFT:
                for i in range(right, left - 1, -1):
                    traversal.append(mtx[down][i])
                down -= 1
                direction = Matrix.UP
            elif direction == Matrix.UP:
                for j in range(down, up - 1, -1):
                    traversal.append(mtx[j][left])
                left += 1
                direction = Matrix.RIGHT

        return traversal


print(
    Matrix.spiral_traverse(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
    )
)

print(
    Matrix.spiral_traverse(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    )
)

print(
    Matrix.spiral_traverse(
        [[32, 44, 27, 23], [54, 28, 50, 62]]
    )
)