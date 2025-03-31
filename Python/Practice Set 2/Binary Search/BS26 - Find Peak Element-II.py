# Problem link - https://www.geeksforgeeks.org/find-peak-element-2d-array/
# Solution - https://www.youtube.com/watch?v=nGGp5XBzC4g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=28


class Solution:
    @staticmethod
    def find_peak(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            x, y = Solution._get_max_cell(mtx, mid, n, m)
            if Solution._is_peak(mtx, x, y, n, m):
                return x, y
            elif mtx[x][y - 1] > mtx[x][y]:
                high = mid - 1
            elif mtx[x][y + 1] > mtx[x][y]:
                low = mid + 1
            else:
                low = mid + 1
        return -1

    @staticmethod
    def _get_max_cell(mtx, mid, n, m):
        max_val, max_idx = -1e6, -1
        for i in range(n):
            if mtx[i][mid] > max_val:
                max_val = mtx[i][mid]
                max_idx = i
        return max_idx, mid

    @staticmethod
    def _is_peak(mtx, x, y, n, m):
        elem = mtx[x][y]
        is_peak = False
        if 0 <= y - 1 < m:
            if 0 <= y + 1 < m:
                if mtx[x][y - 1] < elem and mtx[x][y + 1] < elem:
                    return True
                else:
                    return False
            else:
                return mtx[x][y - 1] < elem
        elif 0 <= y + 1 < m:
            return mtx[x][y + 1] < elem
        else:
            return False


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
