class Solution:
    @staticmethod
    def search(mtx, x):
        n, m = len(mtx), len(mtx[0])
        row, col = 0, m - 1
        while row < n and col >= 0:
            if mtx[row][col] == x:
                return row, col
            if x > mtx[row][col]:
                row += 1
            else:
                col -= 1
        return -1, -1


print(
    Solution.search(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        14
    )
)

print(Solution.search(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(Solution.search(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))

print(
    Solution.search(
        [
            [1, 2, 4, 5],
            [3, 4, 9, 16],
            [7, 10, 14, 29]
        ],
        8
    )
)

print(
    Solution.search(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        5
    )
)
