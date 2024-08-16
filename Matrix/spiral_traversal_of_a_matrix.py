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
        self.build()

    def build(self):
        arr_idx = 0
        for row in range(self.r):
            for col in range(self.c):
                self.mtx[row][col] = self.arr[arr_idx]
                arr_idx += 1

    def get_spiral_traversal(self):
        left, right, up, down = 0, self.c - 1, 0, self.r - 1
        result = []
        traversal_direction = TraversalDirections.RIGHT

        while left <= right and up <= down:
            if traversal_direction == TraversalDirections.RIGHT:
                for i in range(left, right + 1):
                    print(self.mtx[up][i], end=" ")
                traversal_direction = TraversalDirections.DOWN
                up += 1
            elif traversal_direction == TraversalDirections.DOWN:
                for i in range(up, down + 1):
                    print(self.mtx[i][right], end=" ")
                traversal_direction = TraversalDirections.LEFT
                right -= 1
            elif traversal_direction == TraversalDirections.LEFT:
                for i in range(right, left - 1, -1):
                    print(self.mtx[down][i], end=" ")
                traversal_direction = TraversalDirections.UP
                down -= 1
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