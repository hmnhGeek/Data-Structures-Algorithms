# Problem link - https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

from enum import Enum


class TraversalDirections(Enum):
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"
    UP = "up"


class Matrix:
    def __init__(self, raster_scan, num_rows, num_cols):
        self.arr = raster_scan
        self.r = num_rows
        self.c = num_cols
        self.mtx = [[None for _ in range(self.c)] for _ in range(self.r)]

        # build the matrix in constructor only.
        self.build()

    def build(self):
        # in O(m*n) we build this matrix from the raster scan.
        # space consumed is also O(m*n).
        arr_idx = 0
        for row in range(self.r):
            for col in range(self.c):
                self.mtx[row][col] = self.arr[arr_idx]
                arr_idx += 1

    def get_spiral_traversal(self):
        # This whole operation will take O(m*n) time and O(m*n) space if we store the traversal.

        # initialize pointers for the four corners of the matrix
        left, right, up, down = 0, self.c - 1, 0, self.r - 1

        # set the beginning traversal direction as rightward.
        traversal_direction = TraversalDirections.RIGHT

        # while the pointers follow their logical orders
        while left <= right and up <= down:
            # if the traversal is to be done from left to right, then it means that the row must be fixed,
            # and we should print from left to right. Once done, the next direction should be downwards in
            # the next iteration. Also, since this row is traversed, increment the `up` pointer.
            if traversal_direction == TraversalDirections.RIGHT:
                for i in range(left, right + 1):
                    print(self.mtx[up][i], end=" ")
                traversal_direction = TraversalDirections.DOWN
                up += 1

            # if the traversal is to be done from up to down, then it means that the col must be fixed,
            # and we should print from up to down. Once done, the next direction should be leftwards in
            # the next iteration. Also, since this col is traversed, reduce the `right` pointer.
            elif traversal_direction == TraversalDirections.DOWN:
                for i in range(up, down + 1):
                    print(self.mtx[i][right], end=" ")
                traversal_direction = TraversalDirections.LEFT
                right -= 1

            # if the traversal is to be done from right to left, then it means that the row must be fixed,
            # and we should print from right to left. Once done, the next direction should be upwards in
            # the next iteration. Also, since this row is traversed, reduce the `down` pointer.
            elif traversal_direction == TraversalDirections.LEFT:
                for i in range(right, left - 1, -1):
                    print(self.mtx[down][i], end=" ")
                traversal_direction = TraversalDirections.UP
                down -= 1

            # if the traversal is to be done from down to up, then it means that the col must be fixed,
            # and we should print from down to up. Once done, the next direction should be rightwards in
            # the next iteration. Also, since this col is traversed, increment the `left` pointer.
            else:
                for i in range(down, up - 1, -1):
                    print(self.mtx[i][left], end=" ")
                traversal_direction = TraversalDirections.RIGHT
                left += 1


mtx1 = Matrix(
    [i for i in range(1, 17)],
    4,
    4
)

# Expected output: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10
mtx1.get_spiral_traversal()

print()
mtx2 = Matrix(
    [i for i in range(1, 13)],
    3,
    4
)

# Expected output: 1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7
mtx2.get_spiral_traversal()
