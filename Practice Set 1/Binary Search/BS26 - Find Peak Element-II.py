class Solution:
    @staticmethod
    def _get_max_cell_in_col(mtx, mid, n):
        x = 0
        for i in range(n):
            if mtx[i][mid] > mtx[x][mid]:
                x = i
        return x

    @staticmethod
    def find_peak(mtx):
        n, m = len(mtx), len(mtx[0])
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            x = Solution._get_max_cell_in_col(mtx, mid, n)
            left = mtx[x][mid - 1] if 0 <= mid - 1 < m else -1
            right = mtx[x][mid + 1] if 0 <= mid + 1 < m else -1
            if mtx[x][mid] > left and mtx[x][mid] > right:
                return x, mid
            elif mtx[x][mid] < right:
                low = mid + 1
            elif mtx[x][mid] < left:
                high = mid - 1
            else:
                high = mid - 1
        return -1, -1



print(
    Solution.find_peak(
        [[8, 6], [10, 1]]
    )
)

print(
    Solution.find_peak(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(Solution.find_peak([[1, 4], [3, 2]]))
print(Solution.find_peak([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
