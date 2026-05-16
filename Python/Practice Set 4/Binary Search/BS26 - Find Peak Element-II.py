class Solution:
    @staticmethod
    def find_peak(mtx):
        n, m = len(mtx), len(mtx[0])
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            row_idx, possible_peak = Solution._get_possible_peak_index(mtx, mid, n)
            left, right = mtx[row_idx][mid - 1] if 0 <= mid - 1 else -1e6, mtx[row_idx][mid + 1] if mid + 1 < n else -1e6
            if left > possible_peak and possible_peak < right:
                low = mid + 1
            elif left > possible_peak:
                high = mid - 1
            elif possible_peak < right:
                low = mid + 1
            else:
                return row_idx, mid
        return None

    @staticmethod
    def _get_possible_peak_index(mtx, mid, n):
        index, elem = -1, -1e6
        for i in range(n):
            if mtx[i][mid] > elem:
                elem = mtx[i][mid]
                index = i
        return index, elem

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
