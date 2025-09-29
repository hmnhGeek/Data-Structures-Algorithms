class Solution:
    @staticmethod
    def spiral_traversal(mtx):
        n, m = len(mtx), len(mtx[0])
        result = []
        top, left, right, down = 0, 0, m - 1, n - 1
        direction = "R"
        while top <= down and left <= right:
            if direction == "R":
                for i in range(left, right + 1):
                    result.append(mtx[top][i])
                top += 1
                direction = "D"
            elif direction == "D":
                for i in range(top, down + 1):
                    result.append(mtx[i][right])
                right -= 1
                direction = "L"
            elif direction == "L":
                for i in range(right, left - 1, -1):
                    result.append(mtx[down][i])
                down -= 1
                direction = "U"
            else:
                for i in range(down, top - 1, -1):
                    result.append(mtx[i][left])
                left += 1
                direction = "R"
        print(result)


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
