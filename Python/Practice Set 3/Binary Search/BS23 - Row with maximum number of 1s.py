# Problem link - https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
# Solution - https://www.youtube.com/watch?v=SCz-1TtYxDI&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=25


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
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """

        # get the dimensions of the matrix.
        n, m = len(mtx), len(mtx[0])

        # store the count of ones and the resultant index at which the maximum ones are found.
        max1s = 0
        max1s_row_index = -1

        # loop in the matrix rows in n-iterations.
        for i in range(n):
            # get the count of 1s in each row in O(log(m)) time.
            one_count = Solution._ones_count(mtx, i, m)

            # update the resultant variable only if the count of 1s in this row > max ones count.
            if one_count > max1s:
                max1s_row_index = i
                max1s = one_count

        # return the resultant index.
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
