# Problem Link - https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1


class Solution:
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"
    UP = "up"

    @staticmethod
    def spiral_traversal(mtx):
        """
            Overall time complexity is O(mn) and space complexity is O(mn).
        """

        n = len(mtx)
        m = len(mtx[0])

        # define directional pointers.
        left = top = 0
        right = m - 1
        down = n - 1

        # define initial direction
        direction = Solution.RIGHT

        while left <= right and top <= down:
            # if direction is right...
            if direction == Solution.RIGHT:
                # print the top row
                for j in range(left, right + 1):
                    print(mtx[top][j], end=" ")
                # move to next row and change direction to down.
                top += 1
                direction = Solution.DOWN
            elif direction == Solution.DOWN:
                # print the right column
                for i in range(top, down + 1):
                    print(mtx[i][right], end=" ")
                # move to the previous column and change direction to left
                right -= 1
                direction = Solution.LEFT
            elif direction == Solution.LEFT:
                # print the down row
                for j in range(right, left - 1, -1):
                    print(mtx[down][j], end=" ")
                # move to the previous row and change direction to up.
                down -= 1
                direction = Solution.UP
            else:
                # print the left column
                for i in range(down, top - 1, -1):
                    print(mtx[i][left], end=" ")
                # move to next column and change direction to right.
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