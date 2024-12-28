# Problem link - https://leetcode.com/problems/search-a-2d-matrix-ii/
# Solution - https://www.youtube.com/watch?v=9ZbB397jU4k&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=27


class Solution:
    @staticmethod
    def search(mtx, target):
        """
            Time complexity is O(n + m) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        # define the search space.
        row, col = 0, m - 1
        while 0 <= row < n and 0 <= col < m:
            # if the value is at row, col, return them.
            if mtx[row][col] == target:
                return row, col
            # if the target is smaller than (row, col) element, it will not be present in this col.
            if mtx[row][col] > target:
                col -= 1
            else:
                # else, if target > (row, col) element, then it will lie possibly in the next row.
                row += 1
        # return -1s if not found.
        return -1, -1


print(
    Solution.search(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        14
    )
)

print(Solution.search(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(Solution.search(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))

print(
    Solution.search(
        [
            [1, 2, 4, 5],
            [3, 4, 9, 16],
            [7, 10, 14, 29]
        ],
        8
    )
)

print(
    Solution.search(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        5
    )
)