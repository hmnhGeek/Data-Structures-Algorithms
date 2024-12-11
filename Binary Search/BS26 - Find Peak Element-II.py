class Solution:
    @staticmethod
    def _get_max(mtx, mid, n, m):
        max_elem, idx = -1e6, -1
        for i in range(n):
            if mtx[i][mid] > max_elem:
                max_elem = mtx[i][mid]
                idx = i
        return idx

    @staticmethod
    def find_peak(mtx):
        n, m = len(mtx), len(mtx[0])
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            max_elem_row_idx = Solution._get_max(mtx, mid, n, m)
            left = mtx[max_elem_row_idx][mid - 1] if mid - 1 >= 0 else -1
            right = mtx[max_elem_row_idx][mid + 1] if mid + 1 < n else -1
            possible_peak = mtx[max_elem_row_idx][mid]
            if possible_peak > left and possible_peak > right:
                return max_elem_row_idx, mid
            elif left > possible_peak:
                high = mid - 1
            else:
                low = mid + 1
        return None, None


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
