# Problem Link - https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1


class Direction:
    RIGHT = "right"
    LEFT = "left"
    DOWN = "down"
    TOP = "top"


class Solution:
    @staticmethod
    def spiral_traversal(mtx):
        """
            Time complexity is O(nm) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        direction = Direction.RIGHT
        top, down, left, right = 0, n - 1, 0, m - 1
        while top <= down and left <= right:
            if direction == Direction.RIGHT:
                for i in range(left, right + 1):
                    print(mtx[top][i], end=" ")
                top += 1
                direction = Direction.DOWN
            elif direction == Direction.DOWN:
                for i in range(top, down + 1):
                    print(mtx[i][right], end=" ")
                right -= 1
                direction = Direction.LEFT
            elif direction == Direction.LEFT:
                for i in range(right, left - 1, -1):
                    print(mtx[down][i], end=" ")
                down -= 1
                direction = Direction.TOP
            else:
                for i in range(down, top - 1, -1):
                    print(mtx[i][left], end=" ")
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
