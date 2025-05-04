class Solution:
    @staticmethod
    def _ones_count(mtx, i, m):
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if mtx[i][mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return m - low

    @staticmethod
    def get_row_with_maximum_1s(mtx):
        n, m = len(mtx), len(mtx[0])
        max1s = 0
        max1s_row_index = -1
        for i in range(n):
            one_count = Solution._ones_count(mtx, i, m)
            if one_count > max1s:
                max1s_row_index = i
                max1s = one_count
        return max1s_row_index


matrix1 = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1]
]
print(Solution.get_row_with_maximum_1s(matrix1))

matrix2 = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]
print(Solution.get_row_with_maximum_1s(matrix2))

matrix3 = [
    [1, 1],
    [1, 1]
]
print(Solution.get_row_with_maximum_1s(matrix3))

matrix4 = [
    [0, 0, 0],
    [0, 1, 1]
]
print(Solution.get_row_with_maximum_1s(matrix4))

matrix5 = [
    [0, 0],
    [1, 1],
    [0, 0]
]
print(Solution.get_row_with_maximum_1s(matrix5))

matrix6 = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]
print(Solution.get_row_with_maximum_1s(matrix6))

matrix7 = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]
print(Solution.get_row_with_maximum_1s(matrix7))
