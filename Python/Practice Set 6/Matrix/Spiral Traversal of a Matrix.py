class Solution:
    @staticmethod
    def spiral_traversal(mtx):
        n = len(mtx)
        m = len(mtx[0])
        left = top = 0
        right = m - 1
        down = n - 1
        direction = "R"
        result = []
        while left <= right and top <= down:
            if direction == "R":
                for j in range(left, right + 1):
                    result.append(mtx[top][j])
                top += 1
                direction = "D"
            elif direction == "D":
                for i in range(top, down + 1):
                    result.append(mtx[i][right])
                right -= 1
                direction = "L"
            elif direction == "L":
                for j in range(right, left - 1, -1):
                    result.append(mtx[down][j])
                down -= 1
                direction = "U"
            else:
                for i in range(down, top - 1, -1):
                    result.append(mtx[i][left])
                left += 1
                direction = "R"
        return result


print(
    Solution.spiral_traversal(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
    )
)
print(Solution.spiral_traversal([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]))
print(Solution.spiral_traversal([[32, 44, 27, 23], [54, 28, 50, 62]]))
