# Problem link - https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
# Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


class Solution:
    @staticmethod
    def get_count_of_ones(row):
        n =  len(row)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            if row[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return n - low

    @staticmethod
    def get_row_with_maximum_1s(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """
        n = len(mtx)
        row_idx = -1
        max_ones = 0
        for i in range(n):
            ones_count = Solution.get_count_of_ones(mtx[i])
            if ones_count > max_ones:
                max_ones = ones_count
                row_idx = i
        return row_idx


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
