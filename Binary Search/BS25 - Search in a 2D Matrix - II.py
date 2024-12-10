class Solution:
    @staticmethod
    def search(mtx, target):
        n, m = len(mtx), len(mtx[0])
        i, j = 0, m - 1
        while i < n and j >= 0:
            if mtx[i][j] == target:
                return i, j
            if mtx[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


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