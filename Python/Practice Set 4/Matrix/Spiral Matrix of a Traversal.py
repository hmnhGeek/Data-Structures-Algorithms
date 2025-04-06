class Direction:
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"
    UP = "up"


class Solution:
    @staticmethod
    def spiral_traversal(mtx):
        n, m = len(mtx), len(mtx[0])

        # define directional pointers.
        left, right = 0, m - 1
        top, down = 0, n - 1
        direction = Direction.RIGHT

        while left <= right and top <= down:
            # if direction is right...
            if direction == Direction.RIGHT:
                # print the top row
                for i in range(left, right + 1):
                    print(mtx[top][i], end=" ")
                # move to next row and change direction to down.
                top += 1
                direction = Direction.DOWN
            elif direction == Direction.DOWN:
                # print the right column
                for i in range(top, down + 1):
                    print(mtx[i][right], end=" ")
                # move to the previous column and change direction to left
                right -= 1
                direction = Direction.LEFT
            elif direction == Direction.LEFT:
                # print the down row
                for i in range(right, left - 1, -1):
                    print(mtx[down][i], end=" ")
                # move to the previous row and change direction to up.
                down -= 1
                direction = Direction.UP
            elif direction == Direction.UP:
                # print the left column
                for i in range(down, top - 1, -1):
                    print(mtx[i][left], end=" ")
                # move to next column and change direction to right.
                left += 1
                direction = Direction.RIGHT
        print()


Solution.spiral_traversal(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
)

Solution.spiral_traversal([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])

Solution.spiral_traversal([[32, 44, 27, 23], [54, 28, 50, 62]])