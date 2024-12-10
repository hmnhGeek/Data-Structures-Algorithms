class Solution:
    @staticmethod
    def search(mtx, target):
        n, m = len(mtx), len(mtx[0])
        low = 0
        high = n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            row = mid // m
            col = mid % m
            if mtx[row][col] == target:
                return row, col
            if mtx[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1, -1


print(
    Solution.search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 29]
        ],
        23
    )
)