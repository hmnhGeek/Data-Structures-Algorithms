class Solution:
    @staticmethod
    def _get_ones_count(arr, m):
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return m - low

    @staticmethod
    def get_row_with_max_1s(mtx):
        n, m = len(mtx), len(mtx[0])
        row_index = -1
        max_ones = 0
        for i in range(n):
            ones_count = Solution._get_ones_count(mtx[i], m)
            if ones_count > max_ones:
                max_ones = ones_count
                row_index = i
        return row_index


print(Solution.get_row_with_max_1s([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.get_row_with_max_1s([[0, 0], [1, 1]]))
print(Solution.get_row_with_max_1s([[0, 0], [0, 0]]))
print(Solution.get_row_with_max_1s([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.get_row_with_max_1s([[1, 1], [1, 1]]))
