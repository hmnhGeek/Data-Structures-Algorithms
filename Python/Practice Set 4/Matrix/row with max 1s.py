class Solution:
    @staticmethod
    def _get_ones_count(mtx, i, low, high, m):
        arr = mtx[i]
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return m - low

    @staticmethod
    def max1s_row(mtx):
        n, m = len(mtx), len(mtx[0])
        max_1s = 0
        row = -1
        for i in range(n):
            ones_count = Solution._get_ones_count(mtx, i, 0, m - 1, m)
            if ones_count > max_1s:
                row = i
                max_1s = ones_count
        return row


print(Solution.max1s_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max1s_row([[0, 0], [1, 1]]))
print(Solution.max1s_row([[0, 0], [0, 0]]))
print(Solution.max1s_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max1s_row([[1, 1], [1, 1]]))
