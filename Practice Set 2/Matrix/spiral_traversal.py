class Solution:
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"
    UP = "up"

    @staticmethod
    def spiral_traversal(mtx):
        n = len(mtx)
        m = len(mtx[0])
        left = top = 0
        right = m - 1
        down = n - 1
        direction = Solution.RIGHT

        while left <= right and top <= down:
            if direction == Solution.RIGHT:
                for j in range(left, right + 1):
                    print(mtx[top][j], end=" ")
                top += 1
                direction = Solution.DOWN
            elif direction == Solution.DOWN:
                for i in range(top, down + 1):
                    print(mtx[i][right], end=" ")
                right -= 1
                direction = Solution.LEFT
            elif direction == Solution.LEFT:
                for j in range(right, left - 1, -1):
                    print(mtx[down][j], end=" ")
                down -= 1
                direction = Solution.UP
            else:
                for i in range(down, top - 1, -1):
                    print(mtx[i][left], end=" ")
                left += 1
                direction = Solution.RIGHT

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