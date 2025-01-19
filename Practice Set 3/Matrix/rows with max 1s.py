class Solution:
    @staticmethod
    def _find_count(mtx, i, n, m):
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if mtx[i][mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return n - low

    @staticmethod
    def max1s_row(mtx):
        n, m = len(mtx), len(mtx[0])
        row_idx = -1
        count_1s = 0
        for i in range(n):
            ones_count = Solution._find_count(mtx, i, n, m)
            if ones_count > count_1s:
                count_1s = ones_count
                row_idx = i
        return row_idx


print(Solution.max1s_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max1s_row([[0, 0], [1, 1]]))
print(Solution.max1s_row([[0, 0], [0, 0]]))
print(Solution.max1s_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max1s_row([[1, 1], [1, 1]]))
