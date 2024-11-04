# Problem link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


class BinarySearch:
    @staticmethod
    def search(arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1

        return low


class Matrix:
    @staticmethod
    def row_with_max_1s(mtx):
        """
            Time complexity is O(n*log(m)) and space complexity is O(m).
        """

        n, m = len(mtx), len(mtx[0])
        max_row = None
        max_1s = 0

        for i in range(n):
            row = mtx[i]
            idx = BinarySearch.search(row)
            if m - idx > max_1s:
                max_1s = m - idx
                max_row = i

        return max_row


print(
    Matrix.row_with_max_1s(
        [
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ]
    )
)

print(
    Matrix.row_with_max_1s(
        [
            [0, 0],
            [1, 1]
        ]
    )
)

print(
    Matrix.row_with_max_1s(
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 0]
        ]
    )
)

print(
    Matrix.row_with_max_1s(
        [
            [0, 0],
            [0, 0]
        ]
    )
)